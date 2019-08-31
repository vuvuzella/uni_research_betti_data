import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

random.seed()

# Uniformly distributed point data
N = 8500
xs = np.random.uniform(high=10, size=(N))
ys = np.random.uniform(high=10, size=(N))

# number of points
num_points = 5

# min and max radius
min_radius = 0.5
max_radius = 1.1

# generate the x and y values of the random holes
holes_x = np.array([ np.full_like(xs, random.uniform(0, 10)) for x in
    range(num_points)])
holes_y = np.array([ np.full_like(xs, random.uniform(0, 10)) for y in
    range(num_points)])

# generate matrices of the radiuses of each hole
radius = np.array([ np.full_like(xs, random.uniform(0.5,
    max_radius))  for x in range(num_points) ])

hole_1_x = holes_x[0]
hole_1_y = holes_y[0]
radius_1 = radius[0]

# get the distance between the point and the center of the hole
dist = np.sqrt(((holes_x[0] - xs) ** 2) + ((holes_y[0] - ys) ** 2))

# 1 if point is beyond the radius, 0 otherwise
factor = (dist >= (radius_1 ** 2) ).astype(int)

print('hole_y: ', holes_x[0,0])
print('hole_x: ', holes_y[0,0])
print('radius: ', radius_1[0])
print(dist)
print(factor)
print(radius_1)

# zero out the x,y points that are within the radius of the center of 
# the circle
xs = xs * factor
ys = ys * factor

# Plotting the points
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xs, ys)
ax.scatter(hole_1_x, hole_1_y, c='red')
plt.show()

