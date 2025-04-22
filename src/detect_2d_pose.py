import os
import torch
import numpy as np
import cv2
from yacs.config import CfgNode as CN
from models.pose_hrnet import get_pose_net
from config import cfg, update_config
from torchvision import transforms

# Load configuration
update_config(cfg, "models/hrnet_w48_384x288.yaml")

# Initialize HRNet model
model = get_pose_net(cfg, is_train=False)
model.load_state_dict(torch.load("models/pose_hrnet_w48_384x288.pth", map_location='cpu'))
model.eval()

# Preprocessing transformation
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def preprocess_image(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (384, 288))  # HRNet-W48 input resolution
    input_tensor = transform(img).unsqueeze(0)  # Shape: [1, 3, H, W]
    return input_tensor, img

def extract_keypoints_from_heatmap(heatmaps):
    heatmaps = heatmaps.squeeze(0).detach().numpy()
    coords = []
    for i in range(heatmaps.shape[0]):
        idx = np.unravel_index(np.argmax(heatmaps[i]), heatmaps[i].shape)
        coords.append((idx[1], idx[0]))  # (x, y)
    return np.array(coords)

def extract_from_folder(input_dir):
    poses = {}
    for img_file in sorted(os.listdir(input_dir)):
        if img_file.endswith('.jpg') or img_file.endswith('.png'):
            path = os.path.join(input_dir, img_file)
            tensor, _ = preprocess_image(path)
            with torch.no_grad():
                output = model(tensor)
            coords = extract_keypoints_from_heatmap(output[0])
            poses[img_file] = coords
    return poses
