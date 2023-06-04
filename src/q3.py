import pandas as pd

# Read the data
flights = pd.read_csv('https://raw.githubusercontent.com/ds5110/rdata/main/data/flights.csv')

# Combine as unique boolean
unique_key = flights.groupby(['carrier', 'flight', 'year', 'month', 'day']).size().max() == 1

# Print the result
print(unique_key)