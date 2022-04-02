import pandas as pd
import numpy as np

"""d1 = {"a": 100, "b": 200, "c": 300, "d": 400, "e": 800}
print("Original dictionary:")
print(d1)
new_series = pd.Series(d1.values(), index=d1.keys())
new_series = pd.Series(d1)
print("Converted series:")
print(new_series)

np_arr = np.array([2, 4, 6, 8, 10])
s1 = pd.Series(np_arr)
print(s1)

0    [Red, Green, White]
1           [Red, Black]
2               [Yellow]"""

new_s = pd.Series([["Red", "Green", "White"], ["Red", "Black"], ["Yellow"]])

print(new_s.apply(pd.Series).stack().reset_index())
"""  level_0  level_1       0
0        0        0     Red
1        0        1   Green
2        0        2   White
3        1        0     Red
4        1        1   Black
5        2        0  Yellow

drop=True
0       Red
1     Green
2     White
3       Red
4     Black
5    Yellow

without reset
0       Red
1     Green
2     White
3       Red
4     Black
5    Yellow """


s = pd.Series(data=[1, 2, 3, 4, 5], index=["A", "B", "C", "D", "E"])
print("Original Data Series:")
print(s)
s = s.reindex(index=["B", "A", "C", "D", "E"])
print("Data Series after changing the order of index:")
print(s)
