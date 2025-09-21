# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Dataset from Google Colab
from google.colab import files
uploaded = files.upload()

# Load Dataset
data = pd.read_csv('IMDB Dataset.csv')
data.head(5)

# Check for Null Values
print("Null values in each column:\n", data.isnull().sum())

# Plot Histogram for feature 'Runtime'
plt.figure(figsize=(8, 5))
plt.hist(data['Runtime'], edgecolor='black')
plt.ylabel("Count of Movies")
plt.xlabel("Runtime")
plt.title("Histogram of Movie Runtime")
plt.show()

# Plot Histogram for feature 'IMDB_Rating'
plt.figure(figsize=(8, 5))
plt.hist(data['IMDB_Rating'], edgecolor='black')
plt.ylabel("Count of Movies")
plt.xlabel("IMDB Rating")
plt.title("Histogram of IMDB Ratings")
plt.show()

# Define parameter bins for 'Runtime' and plot histogram
bins_time = np.arange(88, 230, 10)
plt.figure(figsize=(8, 5))
plt.hist(data['Runtime'], bins=bins_time, edgecolor='black', color='green')
plt.ylabel("Count of Movies")
plt.xlabel("Runtime")
plt.title("Histogram of Runtime with Custom Bins")
plt.xticks(bins_time)
plt.show()

# Define parameter bins for 'IMDB_Rating' and plot histogram
bins_rating = np.arange(8, 10.2, 0.2)
plt.figure(figsize=(8, 5))
plt.hist(data['IMDB_Rating'], bins=bins_rating, edgecolor='black', color='green')
plt.ylabel("Count of Movies")
plt.xlabel("IMDB Rating")
plt.title("Histogram of IMDB Ratings with Custom Bins")
plt.xticks(bins_rating)
plt.show()
