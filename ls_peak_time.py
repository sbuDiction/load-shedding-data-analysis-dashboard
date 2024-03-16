"""
This file houses the code for creating a a heatmap chart to show load shedding peak times during the day for each day of the week.
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

data = pd.read_csv("EskomSePush Loadshedding History - EskomSePush_history.csv")

# Convert 'created_at' column to datetime
data["created_at"] = pd.to_datetime(data["created_at"])

# Extract day of the week and hour of the day
data["day_of_week"] = data["created_at"].dt.dayofweek
data["hour_of_day"] = data["created_at"].dt.hour

# Group by day of the week and hour of the day and count occurrences of each combination
heatmap_data = data.groupby(["day_of_week", "hour_of_day"]).size().unstack(fill_value=0)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [
    "00:00",
    "01:00",
    "02:00",
    "03:00",
    "04:00",
    "05:00",
    "06:00",
    "07:00",
    "08:00",
    "09:00",
    "10:00",
    "11:00",
    "12:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00",
    "17:00",
    "18:00",
    "19:00",
    "20:00",
    "21:00",
    "22:00",
    "23:00",
]

# Create the heatmap
fig = go.Figure(
    data=go.Heatmap(
        z=heatmap_data.values,
        x=hours,  # Hours of the day
        y=days,  # Days of the week
        colorscale="Viridis",  # Color scale for heatmap
        hovertemplate="Day: %{y}<br>Hour: %{x}<extra></extra>",  # Hover text template
        texttemplate="%{y}",
        textfont={"size": 15},
    )
)

# Update layout
fig.update_layout(
    title="Load Shedding Peak Time",
    xaxis_title="Hour of the Day",
    yaxis_title="Day of the Week",
)

ls_peak_time_chart = fig
