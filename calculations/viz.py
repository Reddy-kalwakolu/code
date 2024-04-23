import pandas as pd
import plotly.express as px

# Load your data
covid_data = pd.read_csv('data/covid_data.csv')
covid_data['date'] = pd.to_datetime(covid_data['date'])

# Group the data by continent and date
continent_time_data = covid_data.groupby(['continent', 'date']).agg({
    'new_cases': 'sum',
    'new_deaths': 'sum'
}).reset_index()

# Visualization for new cases over time by continent
fig_cases = px.line(continent_time_data, x='date', y='new_cases', color='continent',
                    title='New COVID-19 Cases Over Time by Continent',
                    labels={'new_cases': 'New Cases', 'date': 'Date', 'continent': 'Continent'},
                    template='plotly_dark')

# Visualization for new deaths over time by continent
fig_deaths = px.line(continent_time_data, x='date', y='new_deaths', color='continent',
                     title='New COVID-19 Deaths Over Time by Continent',
                     labels={'new_deaths': 'New Deaths', 'date': 'Date', 'continent': 'Continent'},
                     template='plotly_dark')

# Display the figures
fig_cases.show()
fig_deaths.show()
