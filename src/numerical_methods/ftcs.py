# Implements the FTCS solution for 1-D and 2-D heat equation, without source
import numpy as np

zero_func = lambda x, t=0, k=0: 0

def ftcs_diffusion_1d(k, x1, x2, T, initial_condition, dx=1e-2, left_bc=zero_func, right_bc=zero_func, force_unstable=False):
    dt = (dx ** 2) / (k * 1.5) if force_unstable else (dx ** 2) / (k * 3)

    Nx = int((x2 - x1) / dx)
    Nt = int(T / dt)

    Xs = np.linspace(x1, x2, Nx)
    Ts = np.linspace(0, T, Nt)

    X, T = np.meshgrid(Xs, Ts)
    Us = np.zeros(shape=X.shape)

    Us[0] = initial_condition(X[0])
    Us[:, 0] = left_bc(Ts) ### WHY DOES THIS WORK
    Us[:, -1] = right_bc(Ts)

    factor = k * dt / (dx ** 2)

    for i in range(1, len(Ts)):
        for j in range(1, len(Xs) - 1):
            u_prev = Us[i - 1][j - 1]
            u_next = Us[i - 1][j + 1]
            u_curr = Us[i - 1][j]

            Us[i][j] = u_curr + factor * (u_next - 2 * u_curr  + u_prev)

    return Us, Xs, Ts

def ftcs_diffusion_2d(k, x1, x2, y1, y2, T, initial_condition,
                      dx=1e-2, dy=1e-2,
                      left_bc=zero_func, right_bc=zero_func, top_bc=zero_func, bot_bc=zero_func,
                      force_unstable=False):

    cfl_condition = ((dx * dy) ** 2) / (2 * k * (dy ** 2 + dx ** 2))
    dt = cfl_condition * 1.01 if force_unstable else cfl_condition * 0.75

    Nx = int((x2 - x1) / dx)
    Ny = int((y2 - y1) / dy)
    Nt = int(T / dt)

    Xs = np.linspace(x1, x2, Nx)
    Ys = np.linspace(y1, y2, Ny)
    Ts = np.linspace(0, T, Nt)

    X, T, Y = np.meshgrid(Xs, Ts, Ys)
    Us = np.zeros(X.shape)

    Us[0] = initial_condition(X[0, :, :], Y[0, :, :])

    Us[:, 0, :] = top_bc(Xs)  # top/y-min
    Us[:, -1, :] = bot_bc(Xs)  # bottom/y-max
    Us[:, :, 0] = left_bc(Ys)  # left/x-min
    Us[:, :, -1] = right_bc(Ys)  # right/x-max

    alpha = (k * dt) / (dx ** 2)
    beta = (k * dt) / (dy ** 2)

    for l in range(1, Nt):

        U_prev = Us[l - 1, :, :]

        X_diff = (U_prev[2:, 1:-1] - 2 * U_prev[1:-1, 1:-1] + U_prev[:-2, 1:-1])

        Y_diff = (U_prev[1:-1, 2:] - 2 * U_prev[1:-1, 1:-1] + U_prev[1:-1, :-2])

        Us[l, 1:-1, 1:-1] = U_prev[1:-1, 1:-1] + alpha * X_diff + beta * Y_diff

        # for i in range(1, Nx - 1):
        #     for j in range(1, Ny - 1):
        #         x_term = alpha * (Us[l - 1, i + 1, j] - 2 * Us[l - 1, i, j] + Us[l - 1, i - 1, j])
        #
        #         y_term = beta * (Us[l - 1, i, j + 1] - 2 * Us[l - 1, i, j] + Us[l - 1, i, j - 1])
        #
        #         Us[l, i, j] = Us[l - 1, i, j] + x_term + y_term

    return Us, Xs, Ys, Ts