from src.numerical_methods.ftcs import ftcs_diffusion_1d
from src.analysis.plots import animate_line_plot
import matplotlib.pyplot as plt
import numpy as np

initial_condition = lambda x: np.sin(np.pi * x)

def main():
    unstable_Us, unstable_Xs, unstable_Ts = ftcs_diffusion_1d(
        k=1,
        x1=0,
        x2=1,
        T=0.0075,
        initial_condition=initial_condition,
        dx=1e-2,
        force_unstable=True
    )

    animation, fig = animate_line_plot(
        unstable_Us, unstable_Xs, unstable_Ts, 50, '1-D Heat: Unstable FTCS', xlabel='x', ylabel='u'
    )

    plt.show()


if __name__ == '__main__':
    main()