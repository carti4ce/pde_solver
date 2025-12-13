from src.numerical_methods.ftcs import ftcs_diffusion_1d
from src.analysis.plots import animate_line_plot
import matplotlib.pyplot as plt
import numpy as np

def initial_condition(x):
    return np.cos(np.pi * 3 * x)

def main():
    Us, Xs, Ts = ftcs_diffusion_1d(
        k=1,
        x1=0,
        x2=1,
        T=0.1,
        initial_condition=initial_condition,
        left_bc = lambda x, t=0, k=0: 1,
        right_bc = lambda x, t=0, k=0: -1,
    )

    duration = 10  # seconds
    interval = (duration * 1000) / Us.shape[0]

    animation, fig = animate_line_plot(
        Us, Xs, Ts, interval_ms=interval, title='Animated U(x,t) vs. X', xlabel='x', ylabel='U(x,t)', line_color='purple')

    plt.show()

if __name__ == '__main__':
    main()