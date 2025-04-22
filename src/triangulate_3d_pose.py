
import numpy as np

def triangulate(p1, p2, proj1, proj2):
    points_3d = []
    for i in range(p1.shape[0]):
        A = np.array([
            (p1[i,0]*proj1[2]-proj1[0]),
            (p1[i,1]*proj1[2]-proj1[1]),
            (p2[i,0]*proj2[2]-proj2[0]),
            (p2[i,1]*proj2[2]-proj2[1])
        ])
        _, _, V = np.linalg.svd(A)
        X = V[-1]
        points_3d.append(X[:3] / X[3])
    return np.array(points_3d)
