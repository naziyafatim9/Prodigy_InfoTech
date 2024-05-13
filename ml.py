# Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Creating a sample dataset
data = {
    'SquareFootage': [1000, 1500, 1200, 1800, 2000],
    'Bedrooms': [2, 3, 2, 4, 3],
    'Bathrooms': [1, 2, 1, 2, 2],
    'Price': [150000, 200000, 170000, 250000, 270000]
}
df = pd.DataFrame(data)

# Splitting the data into training and testing sets
X = df[['SquareFootage', 'Bedrooms', 'Bathrooms']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Example prediction for a new data point
new_data = [[1600, 3, 2]]  # Square footage: 1600, Bedrooms: 3, Bathrooms: 2
predicted_price = model.predict(new_data)
print(f"Predicted Price for new data: {predicted_price}")