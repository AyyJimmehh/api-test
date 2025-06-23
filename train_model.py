from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train a simple model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save model to 'model.pkl'
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved as model.pkl")
