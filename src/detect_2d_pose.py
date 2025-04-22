
import numpy as np
import os

def simulate_2d_pose(image_path):
    np.random.seed(hash(image_path) % 123456)
    return np.random.randint(50, 200, size=(17, 2))

def extract_from_folder(input_dir):
    poses = {}
    for img_file in sorted(os.listdir(input_dir)):
        if img_file.endswith('.jpg') or img_file.endswith('.png'):
            path = os.path.join(input_dir, img_file)
            pose = simulate_2d_pose(path)
            poses[img_file] = pose
    return poses
