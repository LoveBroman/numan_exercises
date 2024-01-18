import matplotlib.pyplot as plt
import numpy as np

class PolyGon:
    def __init__(self, *corners):
        self.corners = list(corners)
        self.corners = corners
        self.edges = []

        print(corners[0])
        for i in range(len(corners[0])):
                self.edges.append((corners[i -1], corners[i]))

    def plot(self):
        plt.figure(num=0, dpi=120)
        for i in range(len(self.corners)):
            plt.plot([self.edges[i][0][0], self.edges[i][1][0]],
                    [self.edges[i][0][1], self.edges[i][1][1]])
        plt.show()


def dist(pos1, pos2):
   return ((pos1 - pos2) **2).sum()**0.5


class Rectangle(PolyGon):
    def __init__(self, *corners):
        super().__init__(corners)
        self.corners = self.corners[0]
        if dist(corners[0], corners[2]) - dist(corners[0], corners[2]) >= 1e-6 or len(corners) != 4:
            raise ValueError('The provided polygon is not a square')

    def area(self):
        return dist(self.corners[0], self.corners[1]) * dist(self.corners[1], self.corners[2])

    def plot(self):
        super().plot()


triangle = PolyGon(np.array([6, 6]), np.array([3, 3]), np.array([3, 6]))
triangle.plot()
# print(triangle.edges)
#
# plt.figure(num=0, dpi=120)
# plt.plot([triangle.edges[0][0][0], triangle.edges[0][1][0]], [triangle.edges[0][0][1], triangle.edges[0][1][1]])
# plt.plot([triangle.edges[1][0][0], triangle.edges[1][1][0]], [triangle.edges[1][0][1], triangle.edges[1][1][1]])
# plt.plot([triangle.edges[2][0][0], triangle.edges[2][1][0]], [triangle.edges[2][0][1], triangle.edges[2][1][1]])
# #
#  plt.show()


square = Rectangle(np.array([0, 1]), np.array([1, 1]), np.array([1, 0]), np.array([0, 0]))
print(square.corners)
print(dist(square.corners[0], square.corners[1]), dist(square.corners[1], square.corners[2]))
# print(square.corners)
square.plot()
#e = np.append(triangle.corners[-1],triangle.corners[0])


