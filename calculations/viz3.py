import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


covid_data_path = 'data/covid_data.csv'
road_accidents_data_path = 'data/road_accidents_data.csv'

# Load the data
covid_data = pd.read_csv(covid_data_path)
road_accidents_data = pd.read_csv(road_accidents_data_path)

# Process COVID data
covid_data['date'] = pd.to_datetime(covid_data['date'])
covid_data['YearMonth'] = covid_data['date'].dt.to_period('M')
covid_monthly = covid_data.groupby('YearMonth').agg({'new_cases': 'sum', 'new_deaths': 'sum'}).reset_index()

# Process Road Accidents data
road_accidents_data['Accident Date'] = pd.to_datetime(road_accidents_data['Accident Date'])
road_accidents_data['YearMonth'] = road_accidents_data['Accident Date'].dt.to_period('M')
accidents_monthly = road_accidents_data.groupby('YearMonth').agg({'Accident_Index': 'count', 'Number_of_Casualties': 'sum'}).rename(columns={'Accident_Index': 'Total_Accidents'}).reset_index()

# Merge the datasets
combined_data = pd.merge(covid_monthly, accidents_monthly, on='YearMonth', how='inner')

# Plotly visualization for Road Accidents over time
accidents_over_time = road_accidents_data.groupby(road_accidents_data['Accident Date'].dt.date).size().reset_index(name='Number of Accidents')
fig = px.line(accidents_over_time, x='Accident Date', y='Number of Accidents', title='Number of Road Accidents Over Time (Interactive)')
fig.write_html('./road_accidents_over_time.html', full_html=False, include_plotlyjs='cdn')

# Matplotlib visualization for COVID cases vs Road Accidents
fig, ax1 = plt.subplots(figsize=(14, 7))
ax1.set_xlabel('Year-Month')
ax1.set_ylabel('New COVID-19 Cases', color='tab:red')
ax1.plot(combined_data['YearMonth'].astype(str), combined_data['new_cases'], color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.set_ylabel('Total Road Accidents', color='tab:blue')
ax2.plot(combined_data['YearMonth'].astype(str), combined_data['Total_Accidents'], color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')
fig.suptitle('Monthly Trends of COVID-19 Cases vs. Road Accidents')
plt.xticks(rotation=45)
fig.canvas.draw()
fig.savefig('./covid_vs_accidents.png')

# Matplotlib visualization for COVID deaths vs Road Casualties
fig, ax1 = plt.subplots(figsize=(14, 7))
ax1.set_xlabel('Year-Month')
ax1.set_ylabel('New COVID-19 Deaths', color='tab:green')
ax1.plot(combined_data['YearMonth'].astype(str), combined_data['new_deaths'], color='tab:green')
ax1.tick_params(axis='y', labelcolor='tab:green')

ax2 = ax1.twinx()
ax2.set_ylabel('Number of Road Casualties', color='tab:purple')
ax2.plot(combined_data['YearMonth'].astype(str), combined_data['Number_of_Casualties'], color='tab:purple')
ax2.tick_params(axis='y', labelcolor='tab:purple')
fig.suptitle('Monthly Trends of COVID-19 Deaths vs. Road Casualties')
plt.xticks(rotation=45)
fig.canvas.draw()
fig.savefig('./covid_deaths_vs_casualties.png')


