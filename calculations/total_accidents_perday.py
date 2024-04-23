import pandas as pd
import plotly.express as px
import plotly.offline as pyo
# Load your dataset
road_accidents_data = pd.read_csv('data/road_accidents_data.csv')

# Ensure the 'Accident Date' column is in datetime format
road_accidents_data['Accident Date'] = pd.to_datetime(road_accidents_data['Accident Date'], errors='coerce')

# Group data by 'Accident Date' and count the number of accidents per day
accidents_over_time = road_accidents_data.groupby(road_accidents_data['Accident Date'].dt.date).size()

# Convert the grouped data into a DataFrame for better compatibility with Plotly
accidents_over_time_df = accidents_over_time.reset_index()
accidents_over_time_df.columns = ['Date', 'Number of Accidents']

# Creating an interactive line plot with Plotly Express
fig = px.line(accidents_over_time_df, x='Date', y='Number of Accidents', title='Number of Road Accidents Over Time (Interactive)')
fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Number of Accidents')
# fig.show()
pyo.plot(fig, filename='plot.html')


