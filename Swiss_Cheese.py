#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt
import random
# get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


N = 10 # number of random centroids
size = 10
radius = 1.5
interval = 0.05

def isNearCentroid(centroids, x, y, z=None):
    for centroid in centroids:
        xDiff = abs(x - centroid[0])
        yDiff = abs(y - centroid[1])
        if z is not None:
            zDiff = abs(z - centroid[2])
        else:
            zDiff = 0
        eDist = math.sqrt((xDiff ** 2) + (yDiff ** 2) + (zDiff ** 2))
        if eDist < radius:
            return True
    return False


# # In[4]:
# 
# dataPoints = np.arange(-size, size, interval)
# meshX, meshY = np.meshgrid(dataPoints, dataPoints)
# 
# centroids2D = []
# 
# # populate the centroids
# for num in range(N):
#     x = random.randint(-size, size)
#     y = random.randint(-size, size)
#     centroids2D.append((x, y))
# 
# pred = []
# for row in dataPoints:
#     for col in dataPoints:
#         if isNearCentroid(centroids2D, row, col) is True:
#             pred.append('y')
#         else:
#             pred.append('b')
#         
# print(len(pred))
# 
# 
# # In[28]:
# 
# 
# # create visualization of a grid
# # fig = plt.figure()
# # plot = fig.add_subplot(4,4,1)
# plt.scatter(meshX, meshY, c=pred)
# plt.show()


# In[28]:


# Produce 3D data
from mpl_toolkits.mplot3d import Axes3D

centroids3D = []

size = 5
dataPoints = np.arange(-size, size, 0.9)

meshX, meshY, meshZ = np.meshgrid(dataPoints, dataPoints, dataPoints)

for num in range(N):
    x = random.randint(-size, size)
    y = random.randint(-size, size)
    z = random.randint(-size, size)
    centroids3D.append((x, y, z))

# 0(n^3) execution time: takes awhile!
pred3D = []
bluePred = []
blueX = []
blueY = []
blueZ = []
yellowX = []
yellowY = []
yellowZ = []
yellowPred = []

for x in dataPoints:
    for y in dataPoints:
        for z in dataPoints:
            if isNearCentroid(centroids3D, x, y, z) is True:
                yellowX.append(x)
                yellowY.append(y)
                yellowZ.append(z)
                yellowPred.append('y')
                pred3D.append('y')
            else:
                blueX.append(x)
                blueY.append(y)
                blueZ.append(z)
                bluePred.append('b')
                pred3D.append('b')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(yellowX, yellowY, yellowZ, c=yellowPred, alpha=0.8)
# ax.scatter(blueX, blueY, blueZ, c=bluePred, alpha=0.2)

plt.show()


# In[ ]:





# In[ ]:




