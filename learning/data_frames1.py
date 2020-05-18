# data_frames1.py

import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)
arr = np.array(np.random.randn(4, 4))
print(arr)
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
data = pd.DataFrame(arr, x, y)
print(data)
print(data[(data[1] > 0) & (data[2] > 0)])
k = 'shan raja kanna ram'.split()
data['alpha'] = k
print(data.set_index('alpha', inplace=True))
print(data)
