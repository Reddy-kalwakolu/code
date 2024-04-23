import pandas as pd
import plotly.express as px
import plotly.offline as pyo
# Load your dataset
data = pd.read_csv('data/covid_data.csv')

# Selecting countries
selected_countries = ['United States', 'India', 'Brazil', 'Italy']

# Filtering the dataset for the selected countries
filtered_data = data[data['location'].isin(selected_countries)]

# Grouping the data by location and summing up new cases and new deaths
country_totals = filtered_data.groupby('location')[['new_cases', 'new_deaths']].sum().reset_index()

# Creating an interactive stacked bar chart with customized tooltips
fig = px.bar(country_totals, x='location', y=['new_cases', 'new_deaths'],
             labels={'value': 'Count', 'variable': 'Type'},
             title='Interactive Total New Cases and New Deaths for Selected Countries',
             hover_data={'location': False})  # Hides the country name in tooltip

# Updating the layout for better visualization
fig.update_layout(barmode='stack',
                  xaxis_title='Country',
                  yaxis_title='Total Number of Cases/Deaths',
                  legend_title_text='Data')

# Updating the tooltips to show only the count for each part of the stacked bar
fig.update_traces(hovertemplate='%{y}')

# Showing the figure
pyo.plot(fig, filename='plot.html')
