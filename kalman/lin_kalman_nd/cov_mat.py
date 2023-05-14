import numpy as np

x = np.array([2,3,-1,4])
y = np.array([8,7,9,6])

c = np.cov(x, y)

print(c)