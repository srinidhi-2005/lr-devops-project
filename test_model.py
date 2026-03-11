import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6])

def test_coefficient():
    model = LinearRegression()
    model.fit(X, y)
    assert round(model.coef_[0], 2) == 2.0

def test_intercept():
    model = LinearRegression()
    model.fit(X, y)
    assert round(model.intercept_, 2) == 0.0

def test_predictions():
    model = LinearRegression()
    model.fit(X, y)
    pred = model.predict([[5]])
    assert round(pred[0], 2) == 10.0
