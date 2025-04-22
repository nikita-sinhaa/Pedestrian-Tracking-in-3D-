# 🚶‍♂️ Pedestrian Tracking in 3D Using Multi-View Pose Estimation

## 🎯 Project Overview
This master's-level project simulates a **real-time pedestrian tracking system** in 3D space using image-based pose estimation and multi-view geometry. The pipeline mimics smart surveillance systems and motion tracking setups used in autonomous navigation and behavioral analysis.

The system:
- Simulates 2D human joint detection from multiple camera views
- Reconstructs 3D joint coordinates using triangulation
- Applies a Kalman Filter for trajectory smoothing
- Generates interactive 3D plots of tracked movement

---

## 🧠 Key Features
- ✅ Simulated 2D pose detection (e.g., COCO-style 17 joints)
- ✅ Triangulation of 3D joint positions from multiple camera perspectives
- ✅ Kalman Filter for temporal stability
- ✅ CSV-based pipeline with no real camera or hardware required
- ✅ 3D trajectory visualization using Plotly

---

## 🧱 Folder Structure

```
Pedestrian3D_Tracking/
├── data/
│   └── multi_view_input/          # Multi-camera simulated frames
├── models/
│   └──  pose_hrnet.py – HRNet model definition
|   └──  hrnet_w48_384x288.yaml – Config file for the W48 model
|   └──  pose_hrnet_w48_384x288.pth – Slot for the actual pretrained weights.
├── src/
│   ├── detect_2d_pose.py          # Simulated 2D joint detection
│   ├── triangulate_3d_pose.py     # Triangulation logic
│   ├── track_kalman.py            # Kalman smoothing
│   ├── visualize_3d_trajectory.py # 3D plotting
│   └── utils.py                   # CSV I/O helpers
├── output/
│   ├── poses_3d.csv               # Smoothed 3D joint logs
│   ├── tracking_log.csv           # Optional log
│   └── 3d_tracking_plot.html      # Final interactive plot
```

---

## 🔁 Pipeline Flow

flowchart LR
    A[Multi-View Input Images] --> B[2D Pose Detection]
    B --> C[Triangulate 3D Pose]
    C --> D[Apply Kalman Filter]
    D --> E[CSV Logs + 3D Plot Output]
```

---

## 📦 How to Run

1. 🟩 Simulate 2D poses:
```bash
python src/detect_2d_pose.py
```

2. 🟨 Triangulate 3D coordinates:
```bash
python src/triangulate_3d_pose.py
```

3. 🟧 Apply Kalman Filter:
```bash
python src/track_kalman.py
```

4. 🟦 Visualize final trajectory:
```bash
python src/visualize_3d_trajectory.py
```

---

## 📈 Sample Output
- `poses_3d.csv`: Time-series 3D joint positions (17 joints)
- `3d_tracking_plot.html`: Interactive 3D animation viewable in browser

---

## 📚 References
- Human3.6M dataset: [http://vision.imar.ro/human3.6m/](http://vision.imar.ro/human3.6m/)
- COCO keypoints format
- Multi-view geometry (Hartley & Zisserman)

---

## 👩‍💻 Author
**Nikita Sinha** 
-🔧 Firmware & Embedded Systems | M.S. Electrical and Computer Engineering
