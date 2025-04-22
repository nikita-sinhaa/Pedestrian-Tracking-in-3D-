
import numpy as np
import plotly.graph_objects as go
import pandas as pd

def visualize_3d_trajectory(file):
    data = pd.read_csv(file)
    fig = go.Figure()
    for j in range(17):
        fig.add_trace(go.Scatter3d(
            x=data[f"X{j}"], y=data[f"Y{j}"], z=data[f"Z{j}"],
            mode='lines+markers',
            name=f"Joint {j}"
        ))
    fig.update_layout(title="3D Pedestrian Tracking Trajectory",
                      scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))
    fig.write_html("../output/3d_tracking_plot.html")
