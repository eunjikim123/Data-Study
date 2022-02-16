import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

plt.plot(bike_sharing["dteday"], bike_sharing["casual"], label = 'Casual')
plt.plot(bike_sharing["dteday"], bike_sharing["registered"], label = 'Registered')

plt.xticks(rotation=30)
plt.ylabel("Bikes Rented")
plt.xlabel("Date")
plt.title("Bikes Rented: Casual vs. Registered")
plt.legend()
plt.show()
