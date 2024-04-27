import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
covid_data = pd.read_csv('./data/covid_data.csv')
road_accidents_data = pd.read_csv('./data/road_accidents_data.csv')

# Filter UK data from the COVID dataset
uk_covid_data = covid_data[covid_data['location'] == 'United Kingdom']

# Convert the date to datetime and aggregate new cases per day
uk_covid_data['date'] = pd.to_datetime(uk_covid_data['date'])
uk_covid_cases_daily = uk_covid_data.groupby('date')['new_cases'].sum().reset_index()

# Ensure the correct column name for road accidents data, and convert it to datetime
road_accidents_data['Accident Date'] = pd.to_datetime(road_accidents_data['Accident Date'])
road_accidents_daily = road_accidents_data.groupby('Accident Date').size().reset_index(name='Total_Accidents')

# Visualize the comparison of daily new COVID cases and road accidents in the UK
fig, ax1 = plt.subplots(figsize=(14, 7))
color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('New COVID Cases', color=color)
ax1.plot(uk_covid_cases_daily['date'], uk_covid_cases_daily['new_cases'], color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Total Road Accidents', color=color)
ax2.plot(road_accidents_daily['Accident Date'], road_accidents_daily['Total_Accidents'], color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.title('Comparison of Daily New COVID Cases and Road Accidents in the UK')
fig.savefig('./visualizations/uk_covid_vs_accidents.png', bbox_inches='tight')

# Highlight the timeline between October 2021 to March 2022
highlight_start = pd.to_datetime('2021-10-01')
highlight_end = pd.to_datetime('2022-03-31')
fig, ax1 = plt.subplots(figsize=(14, 7))
ax1.set_xlabel('Date')
ax1.set_ylabel('New COVID Cases', color=color)
ax1.plot(uk_covid_cases_daily['date'], uk_covid_cases_daily['new_cases'], color=color)
ax1.fill_between(uk_covid_cases_daily['date'], uk_covid_cases_daily['new_cases'], where=(uk_covid_cases_daily['date'] >= highlight_start) & (uk_covid_cases_daily['date'] <= highlight_end), color=color, alpha=0.3)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
ax2.set_ylabel('Total Road Accidents', color=color)
ax2.plot(road_accidents_daily['Accident Date'], road_accidents_daily['Total_Accidents'], color=color)
ax2.fill_between(road_accidents_daily['Accident Date'], road_accidents_daily['Total_Accidents'], where=(road_accidents_daily['Accident Date'] >= highlight_start) & (road_accidents_daily['Accident Date'] <= highlight_end), color=color, alpha=0.3)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.title('Comparison of Daily New COVID Cases and Road Accidents in the UK (Highlight Oct 2021 - Mar 2022)')
fig.savefig('./visualizations/uk_covid_vs_accidents_highlight.png', bbox_inches='tight')

# Optional: Display the figures
# plt.show()

# Provide file paths for download or web use
print("Saved visualizations at:")
print("./visualizations/uk_covid_vs_accidents.png")
print("./visualizations/uk_covid_vs_accidents_highlight.png")
