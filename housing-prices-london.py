import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.tree import DecisionTreeRegressor
import os

London_Housing_file_data = "../London-housing-dataset.csv"
house_data = pd.read_csv(London_Housing_file_data)

#From data columns, store the input columns into a list
feature_inputs = ["Area in sq ft", "No. of Bedrooms", "No. of Bathrooms"] 

X = house_data[feature_inputs]  # use the input list as our inputs
y = house_data.Price # store the expected value (Price) into a new variable (y)

#create a model and assign a random number to ensure same result on every run
London_model = DecisionTreeRegressor(random_state = 7)
#Fit data into model
London_model.fit(X, y) #where X is our input and y is our desired output

print("Predicted Price :" , end=" ")
# Print the top 5 result of the predicted price column
print(London_model.predict(X.head()))
# Print the top 5 result of the original price column
print(house_data.Price.head())

