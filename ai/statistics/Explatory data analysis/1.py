# 📦 Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 📂 Import Dataset
from google.colab import files
uploaded = files.upload()  # This will prompt you to upload the CSV file

# Load dataset
data = pd.read_csv('Titanic Dataset.csv')
data.head(5)

# Passengers belonging to which Gender survived the most
sns.countplot(x='Sex', hue='Survived', data=data)
plt.title("Survival Count by Gender")
plt.show()

# Passengers from which PClass survived the most and the least
sns.countplot(x='Pclass', hue='Survived', data=data)
plt.title("Survival Count by Passenger Class")
plt.show()

# Highest number of passengers belong to which Age group
sns.histplot(data['Age'], bins=40, kde=False)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.show()

# Highest number of passengers belong to which Gender
sns.countplot(x='Sex', data=data)
plt.title("Gender Distribution of Passengers")
plt.show()

# Is SibSp (siblings\spouse aboard) associated with Survived
sns.countplot(x='Survived', hue='SibSp', data=data, palette='mako')
plt.title("Survival Count by SibSp")
plt.show()

# Is Parch (parents\children aboard) associated with Survived
sns.countplot(x='Survived', hue='Parch', data=data, palette='mako')
plt.title("Survival Count by Parch")
plt.show()

# Is Fare normally distributed
sns.histplot(data['Fare'], kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.show()

# Check the age group of majority of people in PClass 1
sns.boxplot(x='Pclass', y='Age', data=data, palette='winter')
plt.title("Age Distribution by Passenger Class")
plt.show()

# Correlation heatmap with Survived feature
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

