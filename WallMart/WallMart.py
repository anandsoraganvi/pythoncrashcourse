
# data analysis
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
train_df = pd.read_csv('train.csv')
weather_df = pd.read_csv('weather.csv')
key_df = pd.read_csv('key.csv')
print(train_df.head())
comb_1_df = pd.merge(key_df, weather_df, on='station_nbr')
print(comb_1_df.head())

comb_2_df = pd.merge(train_df, comb_1_df, on=['store_nbr', 'date'])
print(comb_2_df.head())

train_final_y_df = comb_2_df['units']
# print(len(train_final_y_df))
train_final_x_df = comb_2_df.drop(['station_nbr', 'units'], axis=1)
# print(train_final_x_df.info())
#lm.fit(train_final_x_df, train_final_y_df)
# print(lm.intercept_)
