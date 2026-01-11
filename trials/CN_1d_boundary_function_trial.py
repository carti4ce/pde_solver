from src.numerical_methods.crank_nicolson import crank_nicolson_1d
from src.analysis.plots import animate_line_plot
import matplotlib.pyplot as plt
import numpy as np

def initial_condition(x):
    return np.sin(np.pi * x)

def left_bc(t):
    return 1 / 2 * np.sin(np.pi * t) + 0.5

def main():
    Us, Xs, Ts = crank_nicolson_1d(
        k=0.1, x1=0, x2=1, T=5, Nx=500, Nt=1000, initial_condition=initial_condition, left_bc=left_bc
    )

    duration = 25  # seconds
    interval = (duration * 1000) / Us.shape[0]

    animation, fig = animate_line_plot(
        Us, Xs, Ts, interval_ms=interval, title='Evolution of u(x,t)', xlabel='x', ylabel='u(x,t)',
        line_color='purple')

    animation.save(
        "sin_bc_animation.gif",
        writer="pillow",
        fps=1000 // interval  # matches interval_ms=50
    )

    plt.show()

if __name__ == '__main__':
    main()