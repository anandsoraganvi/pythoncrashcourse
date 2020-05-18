# data analysis
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
train_df = pd.read_csv('train.csv')
weather_df = pd.read_csv('weather.csv')
key_df = pd.read_csv('key.csv')
print(train_df.head())

few_comb2_df =comb_2_df.head(10000)
few_comb2_df.head(10)

#Data finishing
#fiinding any missing data in tmax,tmin and tavg

few_comb2_df_tmax=few_comb2_df[few_comb2_df['tmax']=='M']
print(few_comb2_df_tmax)
#output as zero rows


few_comb2_df_tmin=few_comb2_df[few_comb2_df['tmin']=='M']
print(few_comb2_df_tmin)

#output as zero rows

few_comb2_df_tavg=few_comb2_df[few_comb2_df['tavg']=='M']
print(few_comb2_df_tavg.head())

#output as 223 rows

#replace mssing data of tavg with average of tmin and tmax 
few_comb2_df_tavg=few_comb2_df[few_comb2_df['tavg']=='M']
few_comb2_df_tavg['tavg']=((few_comb2_df_tavg['tmax'].astype(int)+few_comb2_df_tavg['tmin'].astype(int))/2).astype(int)
print(few_comb2_df_tavg['tavg'])