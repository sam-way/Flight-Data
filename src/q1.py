import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data 
filepath = 'https://raw.githubusercontent.com/ds5110/rdata/main/data/flights.csv'
flights = pd.read_csv(filepath)

#Plot, show, save
sns.jointplot(x='distance', y='arr_delay', data=flights)
plt.savefig("figs/q1FullSet.png")
plt.show()


