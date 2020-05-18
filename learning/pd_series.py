import pandas as pd
import numpy as np

lisa = [10, 203, 23]
cahr = ['a', 'b', 'c']
dict_1 = {"shan": 1, "sany": 2, "gokul": 3}

arr = np.array(lisa)

set1 = pd.Series(dict_1)
set2 = pd.Series([1, 2, 3], ['India', 'Tamilnadu', 'kerala'])
set3 = pd.Series([1, 2, 5], ['India', 'Tamilnadu', 'China'])
print(set2 + set3)
