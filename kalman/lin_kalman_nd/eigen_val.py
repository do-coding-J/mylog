import numpy as np

c = np.array([[5,-2], [-2,1]])

eigenVal, eigenVec = np.linalg.eig(c)

a = np.sqrt(eigenVal[0])
b = np.sqrt(eigenVal[1])

theta = np.arctan(eigenVec[1, 0]/eigenVec[0, 0])
