
import numpy as np
import pandas as pd

def save_3d_poses_to_csv(poses, file):
    data = {}
    for j in range(poses.shape[1]):
        data[f"X{j}"] = poses[:, j, 0]
        data[f"Y{j}"] = poses[:, j, 1]
        data[f"Z{j}"] = poses[:, j, 2]
    df = pd.DataFrame(data)
    df.to_csv(file, index=False)
