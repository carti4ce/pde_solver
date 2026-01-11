from src.grid.grid import Grid
import numpy as np

class CartesianGrid(Grid):
    def __init__(self, domain, points):
        """
        :param domain: of the form ((x1,x1), (y1,y2), ...)
        :param points: tuple containing the number of points in each dimension (xs, ys, zs)
        """
        self.domain = domain
        self.dim = self.get_dim()
        self.points = points

        if self.dim != len(self.points): raise IndexError("Points tuple should be same dimension as space domain")
        if self.dim == 1: self.domain = (self.domain, )


    def make_grid(self):

        axes = [
            np.linspace(self.domain[i][0], self.domain[i][1], self.points[i])
            for i in range(self.dim)
        ]
        grid = np.meshgrid(*axes, indexing="ij")

        self.coords = grid
        self.grid_tensor = np.stack(grid)