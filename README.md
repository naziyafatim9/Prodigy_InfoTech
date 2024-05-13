# Prodigy_InfoTech
Task1
To implement a linear regression model for predicting house prices based on square footage, number of bedrooms, and number of bathrooms, follow these steps:

Gather Data: Collect a dataset containing information about houses, including their square footage, number of bedrooms, number of bathrooms, and corresponding prices.

Preprocess Data: Clean the dataset by handling missing values, outliers, and any data inconsistencies. Normalize or scale the numerical features like square footage, bedrooms, and bathrooms if needed.

Split the Data: Divide the dataset into training and testing sets. Typically, a common split is 80% for training and 20% for testing.
Choose the Model: Select a linear regression model from libraries like scikit-learn in Python. Instantiate the model.

Train the Model: Fit the model to the training data using the fit method. This step involves finding the optimal parameters (coefficients) for the linear regression equation.

Evaluate the Model: Use the testing data to evaluate the model's performance. Calculate metrics such as mean squared error (MSE), mean absolute error (MAE), or R-squared to assess how well the model predicts house prices.

Make Predictions: Once the model is trained and evaluated, use it to make predictions on new data. Provide the model with the square footage, number of bedrooms, and number of bathrooms of a house to predict its price.
