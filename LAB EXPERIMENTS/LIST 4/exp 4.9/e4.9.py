from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

X = iris.data

# Apply PCA
pca = PCA(n_components=2)

X_reduced = pca.fit_transform(X)

print("Original shape:", X.shape)
print("Reduced shape:", X_reduced.shape)

print("Reduced data:")
print(X_reduced[:5])
