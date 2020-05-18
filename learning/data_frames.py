# data_frames.py
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
df_1 = pd.DataFrame(np.random.randn(4, 5), ['a', 'b', 'c', 'd'], [1, 2, 3, 4, 5])
print(df_1)
print(df_1[[3, 5]])
df_1[7] = df_1[1] + df_1[3]
print(df_1[7])
df_1.drop('a', axis=0, inplace=False)
print(df_1.loc[['a', 'd'], [1, 4]])
print(df_1.loc['a', 1])
