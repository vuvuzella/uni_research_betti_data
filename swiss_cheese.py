import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def getEuclidDist(x1, y1, x2, y2):
    return np.sqrt(((x1 - x2) ** 2) + (y1 - y2) ** 2)


def displayPlot(squareSize, radius, circle=None):

    if circle is None:
        return

    c_x, c_y = circle

    actRange = np.arange(0, size, 0.025)
    coordinates = np.array([[x, y] for x in actRange for y in actRange])
    # print(np.array(coordinates)[:, 0].shape)
    print(coordinates.shape)
    mesh_x, mesh_y = np.meshgrid(actRange, actRange)
    dist = getEuclidDist(c_x, c_y, coordinates[:, 0], coordinates[:, 1])
    print(dist)

    # prediction = np.array([ 0 if getEuclidDist(c_x, c_y, coord[], coord[1]) < radius else 1
    #     for coord in coordinates ])

    prediction = (dist > radius).astype(int)
    # reshape_xy = int(sqrt(pred.shape[0]))
    # prediction = np.reshape(pred, (reshape_xy, reshape_xy))
    # y, x = np.where(prediction==1)

    fig = plt.figure(figsize=(squareSize, squareSize))
    plot = fig.add_subplot(1,1,1, title='solid')
    # plot.plot(mesh_x, mesh_y, data=prediction)
    plot.scatter(mesh_x, mesh_y,
            c=['white' if pred == 0 else 'blue' for pred in prediction ])
    plt.show()


if __name__ == '__main__':

    size = 8
    centroid = (size / 2, size / 2)
    radius = 1

    displayPlot(size, radius, centroid)
