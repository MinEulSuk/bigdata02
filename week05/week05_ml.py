import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

df = pd.read_csv('life_satisfaction.csv')

X = df[["GDP per capita (USD)"]].values
y = df[["Life satisfaction"]].values

model1 = LinearRegression()
model2 = KNeighborsRegressor(3)

model1.fit(X, y)
model2.fit(X, y)
new_instance = [[31_721.3]] # South Korea GDP per capita in 2020
print(f'Life Satisfaction(Linear Regression) : {model1.predict(new_instance)}')
print(f'Life Satisfaction(Kneighors Regression) : {model2.predict(new_instance)}')
print(model1.predict(new_instance))
print(model2.predict(new_instance))

