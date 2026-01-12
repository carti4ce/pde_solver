from src.grid.cartesian_grid import CartesianGrid

def main():
    space_domain = (0, 1)
    grid = CartesianGrid(space_dom=space_domain, space_points=(10,), time_dom=(0,1), time_points=5)
    grid.make_grid()
    print(grid.grid_tensor.shape)
    print(grid.grid_tensor[:,3,0])

if __name__ == "__main__":
    main()