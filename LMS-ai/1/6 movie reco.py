# 1. Install Required Libraries
#  pip install pandas scikit-learn nltk
# 2. Import Libraries and Load Data

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem.porter import PorterStemmer
import ast

nltk.download('stopwords')
ps = PorterStemmer()

# Load datasets
movies = pd.read_csv('movies.csv')  # Replace with your dataset path
credits = pd.read_csv('credits.csv')  # Replace with your dataset path

# Merge datasets
movies = movies.merge(credits, on='title')
# 3. Data Preprocessing

# Handle missing values
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies = movies.dropna()

# Convert string representations of lists to actual lists
def convert(text):
    return [i['name'] for i in ast.literal_eval(text)] if isinstance(text, str) else []

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert)
movies['crew'] = movies['crew'].apply(lambda x: [i['name'] for i in ast.literal_eval(x) if i['job'] == 'Director'])

# Combine all metadata into a single 'tags' column
movies['tags'] = movies['overview'] + movies['genres'].apply(lambda x: ' '.join(x)) + \
                  movies['keywords'].apply(lambda x: ' '.join(x)) + \
                  movies['cast'].apply(lambda x: ' '.join(x)) + \
                  movies['crew'].apply(lambda x: ' '.join(x))

# Apply stemming
def stem(text):
    return ' '.join([ps.stem(word) for word in text.split()])

movies['tags'] = movies['tags'].apply(stem)
# 4. Vectorization and Similarity Calculation

# Convert text data into numerical vectors
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(movies['tags']).toarray()

# Compute cosine similarity
similarity = cosine_similarity(vector)
#5. Recommendation Function

def recommend(movie_title):
    try:
        # Find the index of the movie
        idx = movies[movies['title'] == movie_title].index[0]
    except IndexError:
        print("Movie not found!")
        return []

    # Get similarity scores for all movies
    sim_scores = list(enumerate(similarity[idx]))

    # Sort movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 5 most similar movies
    movie_indices = [i[0] for i in sim_scores[1:6]]
    return movies['title'].iloc[movie_indices].tolist()

# Example usage
print(recommend("The Dark Knight"))