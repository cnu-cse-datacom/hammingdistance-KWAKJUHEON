import random
import numpy as np
import pandas as pd
from hamming_parctice import hamming

df = pd.read_csv("sample.csv", names=['word','bin'])

count = 0
min = 1000
i = 0
j = 1
for i in range(0,100):
    for j in range(0,100):
        if i is not j:
            hd = hamming(df.iloc[i,1], df.iloc[j,1])
            print(count, "(", df.iloc[i,0], df.iloc[j,0], ")hamming_distance: ",hd)
            if min > hd:
                min = hd
            count += 1
print("min hamming distance", min)
