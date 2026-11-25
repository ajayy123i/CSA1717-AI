from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)
# Train model
model.fit(X, y)
# Predict
prediction = model.predict([[5.1, 3.5, 1.4, 0.2]])
print("Predicted class:", iris.target_names[prediction[0]])
