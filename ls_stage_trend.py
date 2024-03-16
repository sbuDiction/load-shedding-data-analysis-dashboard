import pandas as pd
import plotly.express as px

# Read the CSV file into a DataFrame
df = pd.read_csv("EskomSePush Loadshedding History - EskomSePush_history.csv")

# Convert the 'created_at' column to datetime format
df["created_at"] = pd.to_datetime(df["created_at"])

# Extract year from the 'created_at' column
df["year"] = df["created_at"].dt.year

# Group by year and frequency the occurrences of each stage
stage_counts = df.groupby(["year", "stage"]).size().reset_index(name="frequency")

# Pivot the table to have years as index and stages as columns
pivot_table = stage_counts.pivot(
    index="year", columns="stage", values="frequency"
).fillna(0)

# Plot the df using Plotly
fig = px.line(
    pivot_table,
    x=pivot_table.index,
    y=pivot_table.columns,
    title="Load Shedding Stage Trends Over the Years",
)
fig.update_layout(xaxis_title="Year", yaxis_title="Frequency", legend_title="Stage")

ls_stage_trend_chart = fig
