from src.grid.grid import Grid
import numpy as np

class CartesianGrid(Grid):
    def __init__(self, space_dom, space_points, time_dom, time_points):
        """
        :param space_dom: of the form ((x1,x1), (y1,y2), ...)
        :param space_points: tuple containing the number of points in each dimension (xs, ys, zs)
        :param time_dom: 2D tuple of the form (t1,t2)
        :param time_points: integer containing the number of temporal dimension points
        """

        self.space_dom = space_dom
        self.time_dom = time_dom
        self.space_points = space_points
        self.time_points = time_points

        self.dim = self.get_dim()

        if self.dim != len(self.space_points): raise IndexError("Points tuple should be same dimension as space domain")
        if self.dim == 1: self.space_dom = (self.space_dom, )


    def make_grid(self):

        axes = [
            np.linspace(self.space_dom[i][0], self.space_dom[i][1], self.space_points[i])
            for i in range(self.dim)
        ]
        axes.append(np.linspace(self.time_dom[0], self.time_dom[1], self.time_points))

        grid = np.meshgrid(*axes, indexing="ij")

        self.coords = grid
        self.grid_tensor = np.stack(grid)
        """
        The form of grid_tensor is [total dimension, x_points, y_points, ..., time_points]
        To grab a point on the grid, index as [:, x_i, y_j, z_k, t_n]
        """