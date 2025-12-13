from src.numerical_methods.ftcs import ftcs_diffusion_2d
from src.analysis.plots import animate_color_plot
import matplotlib.pyplot as plt
import numpy as np

def initial_condition(x, y):
    return np.sin(2 * np.pi * x) * np.sin(2 * np.pi * y)

def main():
    Us, Xs, Ys, Ts = ftcs_diffusion_2d(
        k = 1,
        x1 = 0,
        x2 = 1,
        y1 = 0,
        y2 = 1,
        T = 0.05,
        initial_condition=initial_condition,
        dx = 1e-2,
        dy = 1e-2,
    )

    duration = 1  # seconds (but not really, for some reason)
    interval = (duration * 1000) / Us.shape[0]

    animation, fig = animate_color_plot(
        U=Us, x=Xs, y=Ys, t=Ts,
        title='2D Heat Equation (FTCS)',
        xlabel='x',
        ylabel='y',
        interval_ms=interval
    )

    plt.show()

if __name__ == '__main__':
    main()