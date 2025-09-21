# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Dataset
# from google.colab import files
# uploaded = files.upload()

# Load the dataset
data = pd.read_csv('Titanic Dataset.csv')
print(data.head())

# Mean Value of Age
mean_age = np.mean(data['Age'])
print("Mean Age of Passengers is", mean_age)

# Mean Value of Fare
mean_fare = np.mean(data['Fare'])
print("Mean Fare is", mean_fare)

"""####**Mean Value of Age and Fare**"""
# Mean Value of age
mean_age = np.mean(data['Age'])
print("Mean Age of Passengers is", mean_age)
# Mean Value of Fare
mean_fare = np.mean(data['Fare'])
print("Mean Fare is ", mean_fare)

# Median Value of Age and Fare
median_age = np.median(data['Age'].dropna())  # Drop NaN values
print("Median value of Age:", median_age)

median_fare = np.median(data['Fare'].dropna())
print("Median value of Fare:", median_fare)

# Mode Value of Age and Pclass
mode_age = stats.mode(data['Age'].dropna(), keepdims=True)
print("Mode value of Age:", mode_age.mode[0])

mode_class = stats.mode(data['Pclass'], keepdims=True)
print("Mode value of Pclass:", mode_class.mode[0])

# Mode Value of Categorical Feature - Gender
mode_gender = data['Sex'].value_counts().idxmax()  # Column name is usually 'Sex'
print("Mode of Gender:", mode_gender)