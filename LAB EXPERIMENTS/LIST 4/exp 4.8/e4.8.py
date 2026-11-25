from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target
# Create SVM model
model = SVC(kernel='linear')
# Train model
model.fit(X, y)
# Predict
prediction = model.predict([X[0]])
print("Predicted class:", data.target_names[prediction[0]])
