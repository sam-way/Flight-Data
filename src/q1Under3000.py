import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data 
filepath = 'https://raw.githubusercontent.com/ds5110/rdata/main/data/flights.csv'
flights = pd.read_csv(filepath)

#remove flights over 2000 miles
flights = flights[(flights['distance'] > 0) & (flights['distance'] < 3000)]

sns.jointplot(x='distance', y='arr_delay', data=flights)

#Save and show
plt.savefig("figs/q1Under3000.png")
plt.show()
