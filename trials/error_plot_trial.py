import matplotlib.pyplot as plt
import numpy as np
from src.numerical_methods.ftcs import ftcs_diffusion_1d
from src.numerical_methods.crank_nicolson import crank_nicolson_1d
from src.analysis.plots import color_plot

def test_solution(x, t, k):
    return np.sin(np.pi * x) * np.exp(-(np.pi ** 2) * k * t)

def initial_condition(x):
    return np.sin(np.pi * x)

def plot_errors(k, L1, L2, T, dx, true_function, initial_condition, left_bc, right_bc):

    dt = (dx ** 2) / (k * 3)

    Nx = int((L2 - L1) / dx)
    Nt = int(T / dt)

    ftcs_Us, _, _ = ftcs_diffusion_1d(k, L1, L2, T, initial_condition, dx, left_bc, right_bc)
    nicolson_Us, _, _ = crank_nicolson_1d(k, L1, L2, T, Nx, Nt, initial_condition, left_bc, right_bc)

    Xs = np.linspace(L1, L2, Nx)
    Ts = np.linspace(0, T, Nt)
    X_grid, T_grid = np.meshgrid(Xs, Ts)

    true_Us = true_function(X_grid, T_grid, k)

    ftcs_errors = true_Us - ftcs_Us
    nicolson_errors = true_Us - nicolson_Us
    error_diff = nicolson_errors - ftcs_errors

    vmax = max(
        np.max(ftcs_errors),
        np.max(nicolson_errors)
    )
    vmin = -1 * vmax


    color_plot(ftcs_errors, Xs, Ts, title='FTCS Error', bar_label='E(u,t)', xlabel='x', ylabel='t', cmap='RdBu_r')#vmin=vmin, vmax=vmax)
    color_plot(nicolson_errors, Xs, Ts, title='Nicolson Error', bar_label='E(u,t)', xlabel='x', ylabel='t', cmap='RdBu_r')#, vmin=vmin, vmax=vmax)



if __name__ == '__main__':
    plot_errors(1, 0, 1, 0.2, 1e-2, test_solution, initial_condition, lambda t: 0, lambda t: 0)