# data_frames _2.py
import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)
outside = ['g1', 'g1', 'g1', 'g2', 'g2', 'g2']
inside = [1, 2, 3, 1, 2, 3]
index = list(zip(outside, inside))
index = pd.MultiIndex.from_tuples(index)
df = pd.DataFrame(np.random.randn(6, 2), index, ['A', 'B'])
df.index.names = ['outer', 'inner']
print(df.loc['g2'].loc[1,'B'])
print(df)
print(df.xs(1,level='inner'))
