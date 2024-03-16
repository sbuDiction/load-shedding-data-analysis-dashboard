"""
This file houses the code for creating a a bar chart to shows the stage distribution of load shedding.
Show most common stages, impacting daily life the most.
"""

import pandas as pd
import plotly.express as px

df = pd.read_csv("EskomSePush Loadshedding History - EskomSePush_history.csv")

# Create a Series showing the count of occurrences for each stage
stage_counts = df["stage"].value_counts()

# Create a bar chart with plotly express
bar_chart = px.bar(
    stage_counts,
    x=stage_counts.index,
    y=stage_counts.values,
    title="Stage Distribution of Load Shedding",
)

bar_chart.update_layout(xaxis_title="Stage", yaxis_title="Frequency")

ls_stage_distribution_chart = bar_chart
