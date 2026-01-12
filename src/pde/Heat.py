from src.pde.pdes import PDE
from src.grid.cartesian_grid import CartesianGrid

class HeatEquation(PDE):

    def __init__(self, diff, grid=None, boundary_condition=None, initial_condition=None):

        """
        :param diff: diffusion coefficient
        :param grid: of the type Grid
        :param boundary_condition: of the type BoundaryCondition
        :param initial_condition: of the type InitialCondition
        """

        self.diff = diff
        self.grid = grid
        self.boundary_condition = boundary_condition
        self.initial_condition = initial_condition

        self.dim = self.get_dimension()
