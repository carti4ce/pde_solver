class Grid:

    def __init__(self):
        self.domain = None
        self.dim = None
        self.points = None
        self.grid_tensor = None
        self.coords = None

    def get_dim(self):
        if isinstance(self.domain[0], tuple):
            return len(self.domain)
        else:
            return 1