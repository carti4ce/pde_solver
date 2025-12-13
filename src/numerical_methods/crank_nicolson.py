import numpy as np

zero_func = lambda x, t=0, k=0: 0

def create_tridiagonal_matrix(main_diag, upper_diag, lower_diag):
    n = len(main_diag)
    if len(upper_diag) != n - 1 or len(lower_diag) != n - 1:
        raise ValueError('Dimension Mismatch: Try again')

    matrix = np.diag(main_diag)
    matrix += np.diag(upper_diag, k=1)
    matrix += np.diag(lower_diag, k=-1)
    return matrix

def generate_CN_matrix(main, uplo, corner, n):
    main_diag = np.ones(n) * main
    main_diag[0] = main_diag[-1] = corner

    upper_diag = np.ones(n - 1) * uplo
    lower_diag = np.ones(n - 1) * uplo
    upper_diag[0] = 0
    lower_diag[-1] = 0

    return create_tridiagonal_matrix(main_diag, upper_diag, lower_diag)

def crank_nicolson_1d(k, x1, x2, T, Nx, Nt, initial_condition, left_bc = zero_func, right_bc = zero_func, source = zero_func):
    """
     k:             diffusivity constant
     L1:            left endpoint of spatial interval
     L2:            right endpoint of spatial interval
     T:             final time
     Nx:            number of x points
     Nt:            number of t points
     left_BC:       function of t ONLY
     right_BC:      ^^^^^^^^
     initial_con:   function of x ONLY
     source:        function of x and t
    """
    dx = (x2 - x1) / (Nx - 1)       # maybe change to Nx - 1
    dt = T / (Nt - 1)               # ^^^^^

    Xs = np.linspace(x1, x2, Nx)
    Ts = np.linspace(0, T, Nt)

    alpha = k * dt / (dx ** 2)
    gamma = 2 * (1 + alpha)
    beta = 2 * (1 - alpha)

    A = generate_CN_matrix(gamma, -alpha, 1, Nx)
    B = generate_CN_matrix(beta, alpha, 0, Nx)

    curr_u = initial_condition(Xs)
    U = [curr_u]

    for t in Ts[:-1]: # t loop finds Us for t + 1

        # Apply source term
        curr_source = (source(Xs, t, k) + source(Xs, t + dt, k)) * dt

        # Apply average boundary conditions
        boundary = np.zeros(Nx)
        boundary[0] = (left_bc(t) + left_bc(t + dt)) / 2 #* alpha
        boundary[-1] = (right_bc(t) + right_bc(t + dt)) / 2 #* alpha


        RHS = (B @ curr_u) + curr_source + boundary
        curr_u = np.linalg.solve(A, RHS)
        U.append(curr_u)

    return np.array(U), Xs, Ts