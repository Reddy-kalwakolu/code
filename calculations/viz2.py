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

# Area Chart for New Cases
fig_area_cases = px.area(continent_time_data, x='date', y='new_cases', color='continent',
                         title='COVID-19 New Cases Over Time by Continent',
                         labels={'new_cases': 'New Cases', 'date': 'Date', 'continent': 'Continent'},
                         template='plotly_dark')
fig_area_cases.show()

# Stacked Bar Chart for New Deaths
fig_bar_deaths = px.bar(continent_time_data, x='date', y='new_deaths', color='continent',
                        title='COVID-19 New Deaths Over Time by Continent',
                        labels={'new_deaths': 'New Deaths', 'date': 'Date', 'continent': 'Continent'},
                        template='plotly_dark', barmode='stack')
fig_bar_deaths.show()
