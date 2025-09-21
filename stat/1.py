#  Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#  Load Dataset from Google Colab
from google.colab import files
uploaded = files.upload()

#  Read the dataset
data = pd.read_csv('Titanic Dataset.csv')
data.head(5)

#  Check Data Types
print(data.dtypes)

#  Nominal and Ordinal Categorical Features
# Nominal Categorical Variables
nominal_cat = ['Name', 'Ticket', 'Cabin']

# Ordinal Categorical Variables
ordinal_cat = ['Embarked', 'Gender']

#  Handle Ordinal Feature: Gender
print("\nGender Value Counts:")
print(data['Gender'].value_counts())

# Define gender categories in order
gender_categories = ['Female', 'Male']
data['Gender'] = pd.Categorical(data['Gender'], categories=gender_categories, ordered=True)

# Get median index from encoded categories
median_index = int(np.median(data['Gender'].cat.codes))
median_gender = gender_categories[median_index]
print("Median Gender:", median_gender)

#  Handle Ordinal Feature: Embarked
print("\nEmbarked Value Counts:")
print(data['Embarked'].value_counts())

# Define embarked categories in order
embarked_categories = ['S', 'C', 'Q']  # Most common order: Southampton, Cherbourg, Queenstown
data['Embarked'] = pd.Categorical(data['Embarked'], categories=embarked_categories, ordered=True)

# Get median index from encoded categories
median_index = int(np.median(data['Embarked'].cat.codes))
median_embarked = embarked_categories[median_index]
print("Median Embarked:", median_embarked)
