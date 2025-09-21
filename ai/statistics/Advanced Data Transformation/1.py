# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns

# Import Dataset
from google.colab import files
uploaded = files.upload()

# Read CSV file (fixed quote error)
data = pd.read_csv('Titanic Dataset.csv')
data.head(5)

# Minimum and Maximum Values of Age
minimum_age = data['Age'].min()
print('Minimum Age:', minimum_age)

maximum_age = data['Age'].max()
print('Maximum Age:', maximum_age)

# Creating binned age and giving it a label
bins = [0, 15, 30, 45, 60, 75]
age_labels = ['Young', 'Young Adult', 'Middle Aged', 'Middle-Older Age', 'Senior']
data['binned_age'] = pd.cut(data['Age'], bins, labels=age_labels)

# Display some results
print(data[['binned_age', 'Age']].head())

# Barplot for binned age
data['binned_age'].value_counts().sort_index().plot(kind='bar')
plt.title('Titanic Age Distribution')
plt.xlabel('Age Groups')
plt.ylabel('Count')
plt.show()

# Check distribution and skewness of selected features
labels = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
for label in labels:
    print(f'Distribution of {label}')
    sns.histplot(data[label].dropna(), kde=True)  # Better than distplot (deprecated)
    plt.title(f'Distribution of {label}')
    plt.show()
    
    print(f'Skewness: {data[label].skew()}')

# Log Transform Skewed Features (add +1 to avoid log(0))
data['log_SibSp'] = np.log(data['SibSp'] + 1)
data['log_Parch'] = np.log(data['Parch'] + 1)
data['log_Fare'] = np.log(data['Fare'] + 1)

# Check if transformed features are less skewed
for label in ['log_SibSp', 'log_Parch', 'log_Fare']:
    print(f'Distribution of {label}')
    sns.histplot(data[label], kde=True)
    plt.title(f'Distribution of {label}')
    plt.show()
    
    print(f'Skewness: {data[label].skew()}')
