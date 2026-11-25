from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Create decision tree
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[5.1, 3.5, 1.4, 0.2]])

print("Predicted class:", iris.target_names[prediction[0]])
