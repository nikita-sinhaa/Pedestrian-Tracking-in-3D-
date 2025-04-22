
import numpy as np
from pykalman import KalmanFilter

def smooth_3d_pose(poses):
    n_joints = poses.shape[1]
    smoothed = np.zeros_like(poses)
    for j in range(n_joints):
        kf = KalmanFilter(initial_state_mean=poses[0, j], n_dim_obs=3)
        smoothed[:, j], _ = kf.smooth(poses[:, j])
    return smoothed
