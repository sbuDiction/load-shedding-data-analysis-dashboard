import pandas as pd
import plotly.express as px

# Read the CSV file into a DataFrame
df = pd.read_csv("EskomSePush Loadshedding History - EskomSePush_history.csv")


# Convert the 'created_at' column to datetime format
df["created_at"] = pd.to_datetime(df["created_at"])

# Extract year from the 'created_at' column
df["year"] = df["created_at"].dt.year

# Group by year and count the total occurrences of load shedding events
total_counts = df.groupby("year").size().reset_index(name="frequency")

# Plot the df using Plotly
fig = px.line(
    total_counts, x="year", y="frequency", title="Load Shedding Trend Over the Years"
)
fig.update_layout(xaxis_title="Year", yaxis_title="Frequency")

ls_trend_chart = fig
