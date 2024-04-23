import pandas as pd
import plotly.express as px
import plotly.offline as pyo
# Load your dataset
import pandas as pd
import plotly.express as px

# Load your dataset
road_accidents_data = pd.read_csv('data/road_accidents_data.csv')



# Drop rows where Latitude and Longitude are null
road_accidents_data = road_accidents_data.dropna(subset=['Latitude', 'Longitude'])

# Generate the map
fig = px.scatter_mapbox(road_accidents_data, lat='Latitude', lon='Longitude',
                        color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                        mapbox_style='carto-positron', title='Map of Road Accidents')

# Show the figure
# fig.show()


# Show the figure
# fig.show()

pyo.plot(fig, filename='plot.html')
