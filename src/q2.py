import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Read the data 
filepath = 'https://raw.githubusercontent.com/ds5110/rdata/main/data/flights.csv'
flights = pd.read_csv(filepath)

grouped_flights = flights.groupby('dest')['arr_delay', 'distance'].mean()

sns.scatterplot(x='distance', y='arr_delay', data=grouped_flights)

#Save and show
plt.savefig("figs/q2.png")
plt.show()
