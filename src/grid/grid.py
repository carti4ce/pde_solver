class Grid:

    def __init__(self):
        self.space_dom = None
        self.time_dom = None
        self.dim = None
        self.points = None
        self.grid_tensor = None
        self.coords = None

    def get_dim(self):
        if isinstance(self.space_dom[0], tuple):
            return len(self.space_dom)
        elif isinstance(self.space_dom, tuple):
            return 1
        else:
            raise ValueError("Invalid spatial domain parameter")