import numpy as np
import math 
from statistics import mean, median, stdev
x = np.array([1,2,3,4,5], dtype=int)
y = np.array([12,23,12,20,18], dtype=int)

print(x)
print(y)
print('jonathan')

z = round(1022.22221,6)
print(z)

listx = [1,0,1,1,10,1]

for x in listx:
  print(x)
print("sum: ", sum(listx))
print("max: ", max(listx))
print("min: ", min(listx))

print("mean: ", mean(listx))
print("median: ", median(listx))
print("standard deviation :", stdev(listx))
print("End")
