# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Upload dataset in Google Colab
from google.colab import files
uploaded = files.upload()

# Read Dataset
data = pd.read_csv('Weather Dataset.csv')
print(data.head(5))
data.info()

# Check for Null Values
print("\nNull values in each column:\n", data.isnull().sum())
print("\nNo feature has any null values.\n")

# Mean, Variance, and Standard Deviation of 'Temperature (C)'
mean_temp = np.mean(data['Temperature (C)'])
print("Mean Temperature is:", mean_temp)

var_temp = np.var(data['Temperature (C)'])
print("Variance of Temperature is:", var_temp)

standard_deviation_temp = np.std(data['Temperature (C)'])
print("Standard Deviation of Temperature is:", standard_deviation_temp)

# Mean & Standard Deviation of Temperature (C) for each Month
print("\nMonthly Temperature Statistics:")
for i in range(1, 13):
    month = data[data["month"] == i]["Temperature (C)"]
    print(f"Month {i}:")
    print(f"  Mean Temperature: {np.mean(month):.2f}")
    print(f"  Standard Deviation: {np.std(month):.2f}\n")
