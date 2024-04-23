import pandas as pd

# Load the dataset
file_path = 'covid_data.csv'
covid_data = pd.read_csv(file_path)

# Display the first few rows and a summary of the dataset
covid_data_head = covid_data.head()
covid_data_info = covid_data.info()
covid_data.describe()

# Group the data by date and sum the new_cases to find the global new cases per day
new_cases_over_time = covid_data.groupby('date')['new_cases'].sum()

# Resetting index to make 'date' a column again for easier visualization and analysis later
new_cases_over_time = new_cases_over_time.reset_index()

new_cases_over_time

# Define the path for the new CSV file
output_file_path = 'covid_daily_new_cases.csv'

# Save the dataframe with daily new cases to a CSV file
new_cases_over_time.to_csv(output_file_path, index=False)

output_file_path

