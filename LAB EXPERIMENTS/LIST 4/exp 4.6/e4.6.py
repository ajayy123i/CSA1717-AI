from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
sentences = [
    "I love this product",
    "This is amazing",
    "I hate this product",
    "This is very bad"
]

labels = ["Positive", "Positive", "Negative", "Negative"]

# Convert text into numerical data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Test sentence
test = ["I love this amazing product"]

test_data = vectorizer.transform(test)

# Predict sentiment
result = model.predict(test_data)

print("Sentiment:", result[0])
