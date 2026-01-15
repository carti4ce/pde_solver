from src.boundary_conditions.boundary_condition import BoundaryCondition

class Dirichlet1D(BoundaryCondition):

    def set_boundary_condition(self):
        self.left_boundary = self.conditions[0]
        self.right_boundary = self.conditions[1]

        if self.dim > 1:
            self.bottom_boundary = self.conditions[2]
            self.top_boundary = self.conditions[3]

        if self.dim > 2:
            self.front_boundary = self.conditions[4]
            self.rear_boundary = self.conditions[5]

    def __init__(self, conditions):
        """
        :param conditions: List containing the boundary conditions in the order ['x_0', 'x_n', 'y_0', 'y_n', 'z_0', 'z_n']
        These can be functions
        """
        self.conditions = conditions
        self.dim = len(self.conditions) / 2
        if self.dim not in [1, 2, 3]: raise ValueError("Invalid dimension")

        self.set_boundary_condition()





