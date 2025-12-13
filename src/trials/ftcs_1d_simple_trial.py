from src.numerical_methods.ftcs import ftcs_diffusion_1d
from src.analysis.plots import animate_line_plot
import matplotlib.pyplot as plt
import numpy as np

initial_condition = lambda x: np.sin(np.pi * x)

def main():
    Us, Xs, Ts = ftcs_diffusion_1d(
        k=1,
        x1=0,
        x2=1,
        T=0.3,
        initial_condition=initial_condition,
        dx=1e-2,
        left_bc=lambda t: 0,
        right_bc=lambda t: 0
    )

    duration = 10  # seconds
    interval = (duration * 1000) / Us.shape[0]

    animation, fig = animate_line_plot(
        Us, Xs, Ts, interval_ms=interval, title='Animated U(x,t) vs. X', xlabel='x', ylabel='U(x,t)',
        line_color='purple')

    plt.show()


if __name__ == '__main__':
    main()