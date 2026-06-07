import plotly.express as px
import pandas as pd


def create_gantt(tasks):

    df = pd.DataFrame(tasks)

    fig = px.timeline(
        df,
        x_start="start_time",
        x_end="finish_time",
        y="assigned_resource",
        color="task_id",
        title="Task Gantt Chart"
    )

    fig.update_yaxes(autorange="reversed")

    return fig