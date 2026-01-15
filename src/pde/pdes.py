from src.solvers.cg import ConjugateGradient

class PDE:
    def __init__(self):
        self.boundary_condition = None
        self.initial_condition = None
        self.grid = None
        self.linear_solver = None

    def get_dimension(self):

        if self.grid.dim == self.boundary_condition.dim and self.grid == self.initial_condition.dim:
            return self.grid.dim
        else:
            raise ValueError(f"Dimension mismatch: domain_dimension = {self.grid.dim}, "
                             f"initial_condition = {self.initial_condition},"
                             f"boundary_condition = {self.boundary_condition}")

    def set_linear_solver(self, solver):
        if solver == "cg":
            self.linear_solver = ConjugateGradient()
        else:
            raise NameError(f"Linear solver type {solver} is not supported")