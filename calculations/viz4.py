import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
covid_data = pd.read_csv('./data/covid_data.csv')
road_accidents_data = pd.read_csv('./data/road_accidents_data.csv')

# Filter UK data from the COVID dataset
uk_covid_data = covid_data[covid_data['location'] == 'United Kingdom']
uk_covid_data['date'] = pd.to_datetime(uk_covid_data['date'])
uk_covid_cases_daily = uk_covid_data.groupby('date')['new_cases'].sum().reset_index()
uk_covid_deaths_daily = uk_covid_data.groupby('date')['new_deaths'].sum().reset_index()

# Check for date column in road accidents dataset and process accordingly
date_col = 'Date' if 'Date' in road_accidents_data.columns else 'Accident Date'
road_accidents_data[date_col] = pd.to_datetime(road_accidents_data[date_col])
road_accidents_daily = road_accidents_data.groupby(date_col).size().reset_index(name='Total_Accidents')

# Define the highlight period
highlight_start = pd.to_datetime('2021-10-01')
highlight_end = pd.to_datetime('2022-04-01')

# Filtering data within the highlight period
filtered_uk_covid_cases = uk_covid_cases_daily[(uk_covid_cases_daily['date'] >= highlight_start) & (uk_covid_cases_daily['date'] <= highlight_end)]
filtered_uk_covid_deaths = uk_covid_deaths_daily[(uk_covid_deaths_daily['date'] >= highlight_start) & (uk_covid_deaths_daily['date'] <= highlight_end)]
filtered_road_accidents = road_accidents_daily[(road_accidents_daily[date_col] >= highlight_start) & (road_accidents_daily[date_col] <= highlight_end)]

# First Visualization: New COVID Cases vs. Road Accidents
fig, ax1 = plt.subplots(figsize=(14, 7))
color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('New COVID Cases', color=color)
ax1.plot(filtered_uk_covid_cases['date'], filtered_uk_covid_cases['new_cases'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Total Road Accidents', color=color)
ax2.plot(filtered_road_accidents[date_col], filtered_road_accidents['Total_Accidents'], color=color)
ax2.tick_params(axis='y', labelcolor=color)
plt.title('Daily New COVID Cases and Road Accidents in the UK')
plt.savefig('visualizations/uk_covid_cases_and_accidents.png', bbox_inches='tight')

# Second Visualization: New COVID Deaths vs. Road Accidents
fig, ax1 = plt.subplots(figsize=(14, 7))
color = 'tab:orange'
ax1.set_xlabel('Date')
ax1.set_ylabel('New COVID Deaths', color=color)
ax1.plot(filtered_uk_covid_deaths['date'], filtered_uk_covid_deaths['new_deaths'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Total Road Accidents', color=color)
ax2.plot(filtered_road_accidents[date_col], filtered_road_accidents['Total_Accidents'], color=color)
ax2.tick_params(axis='y', labelcolor=color)
plt.title('Daily New COVID Deaths and Road Accidents in the UK')
plt.savefig('visualizations/uk_covid_deaths_and_accidents.png', bbox_inches='tight')

# Third Visualization: Highlight period with both cases and deaths
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 14))
# Cases
ax1.plot(filtered_uk_covid_cases['date'], filtered_uk_covid_cases['new_cases'], label='New Cases', color='red')
ax1.set_ylabel('New Cases')
ax1.set_title('New COVID Cases during Highlight Period')
ax1.grid(True)
# Deaths
ax2.plot(filtered_uk_covid_deaths['date'], filtered_uk_covid_deaths['new_deaths'], label='New Deaths', color='orange')
ax2.set_ylabel('New Deaths')
ax2.set_title('New COVID Deaths during Highlight Period')
ax2.grid(True)
plt.tight_layout()
plt.savefig('visualizations/uk_covid_cases_deaths_highlight.png', bbox_inches='tight')
