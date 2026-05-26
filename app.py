from flask import Flask
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# training data
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([2,4,6,8,10])

# train model
model = LinearRegression()
model.fit(X, y)

@app.route("/")
def home():

    value = np.array([[6]])
    prediction = model.predict(value)

    return f"Prediction from Linear Regression Model: {prediction[0]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
