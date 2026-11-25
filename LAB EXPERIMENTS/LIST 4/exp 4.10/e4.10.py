import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# User-item rating matrix
data = {
    'Movie1': [5, 4, 0, 1],
    'Movie2': [4, 5, 0, 2],
    'Movie3': [0, 1, 5, 4],
    'Movie4': [1, 0, 4, 5]
}

df = pd.DataFrame(data, index=['User1', 'User2', 'User3', 'User4'])

# Calculate user similarity
similarity = cosine_similarity(df)

print("User Similarity:")
print(similarity)

# Recommend movies for User1
similar_users = similarity[0]

# Find the most similar user
similar_user_index = similar_users[1:].argmax() + 1

# Get recommendations
recommendations = df.iloc[similar_user_index]
recommendations = recommendations[df.iloc[0] == 0]

print("Recommended movies:")
print(recommendations)
