import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
from matplotlib.animation import FuncAnimation
import numpy as np
import scienceplots

plt.style.use(['science', 'notebook'])



def color_plot(U, X, T, title, bar_label, xlabel, ylabel, cmap='plasma', vmin=None, vmax=None):

    plt.figure(figsize=(8, 5))

    plt.imshow(U,
               aspect='auto',
               origin='lower',
               extent=(0, X[-1], 0, T[-1]),
               cmap=cmap,
               vmin=vmin,
               vmax=vmax
            )

    plt.colorbar(label=bar_label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()



def line_plot(U, X, T, num_lines, title, xlabel, ylabel, legend=True, ):
    n = len(T)
    time_points = np.round(np.linspace(0, n - 1, num_lines)).astype(np.int32)

    for i in time_points:
        plt.plot(X, U[i, :], label=f't={T[i]:.2f}')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if legend: plt.legend()
    plt.show()





def animate_line_plot(U, X, T,
                      interval_ms=50,
                      title='Animated U(x, t) vs. X',
                      xlabel='X-axis',
                      ylabel='U(x, t)',
                      line_color='b-', y_lim_padding_factor=1.1):

    T_max = U.shape[0]

    if T_max <= 1:
        print("Error: Need at least 2 time steps for animation.")
        return None, None

    # interval_ms = (total_duration_seconds * 1000) / T_max
    total_duration_seconds = (interval_ms * T_max) / 1000

    print(f"Animation calculated for {T_max} frames over {total_duration_seconds} seconds.")
    print(f"Interval set to {interval_ms:.2f} ms per frame.")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.set_xlim(X.min(), X.max())

    line, = ax.plot(X, U[0, :], line_color, lw=2)

    y0_min = U[0].min()
    y0_max = U[0].max()

    data0_range = y0_max - y0_min
    data0_mid = (y0_max + y0_min) / 2.0
    half_range0 = (data0_range / 2.0) * y_lim_padding_factor

    ax.set_ylim(data0_mid - half_range0, data0_mid + half_range0)

    # Set initial labels and title (using ax.set_title as blit=False works better)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(f'{title} | Step {0} of {T_max - 1}')

    def update(frame):

        new_y_data = U[frame, :]
        line.set_ydata(new_y_data)

        current_min = new_y_data.min()
        current_max = new_y_data.max()
        data_range = current_max - current_min
        data_mid = (current_max + current_min) / 2.0

        new_half_range = (data_range / 2.0) * y_lim_padding_factor

        required_ymin = data_mid - new_half_range
        required_ymax = data_mid + new_half_range

        current_ymin, current_ymax = ax.get_ylim()

        new_ymax = max(required_ymax, current_ymax)

        new_ymin = min(required_ymin, current_ymin)

        ax.set_ylim(new_ymin, new_ymax)

        if data_range < 1e-6 and current_ymax == new_ymax and current_ymin == new_ymin:
            ax.set_ylim(current_min - 0.1, current_max + 0.1)

        ax.set_title(f'{title} | Step {frame} of {T_max - 1}')
        return line,

    anim = FuncAnimation(fig,
                         update,
                         frames=T_max,
                         interval=interval_ms,
                         blit=False,  # False to avoid overlapping text/axes
                         repeat=True)
    return anim, fig





def animate_color_plot(U, x, y, t, title, xlabel, ylabel, interval_ms=50, cmap='viridis'):
    T_max = U.shape[0]

    if T_max <= 1:
        print("Error: Need at least 2 time steps for animation.")
        return None, None

    # interval_ms = (total_duration_seconds * 1000) / T_max
    total_duration_seconds = (interval_ms * T_max) / 1000

    print(f"Animation calculated for {T_max} frames over {total_duration_seconds} seconds.")
    print(f"Interval set to {interval_ms:.2f} ms per frame.")

    fig, ax = plt.subplots(figsize=(8, 6))

    vmin_global = U.min()
    vmax_global = U.max()

    im = ax.imshow(U[0],
                   origin='lower',
                   extent=(x.min(), x.max(), y.min(), y.max()),
                   cmap=cmap,
                   vmin=vmin_global,
                   vmax=vmax_global)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(f'{title} | Step {0} of {T_max - 1}')

    fig.colorbar(im, ax=ax, label='Value of U')

    def update(frame):

        new_data = U[frame]

        im.set_array(new_data)

        ax.set_title(f'{title} | Step {frame} of {T_max - 1}')

        return im,

    anim = FuncAnimation(fig,
                         update,
                         frames=T_max,
                         interval=interval_ms,
                         blit=False,  # CRITICAL
                         repeat=True)

    return anim, fig

    # T_max = U.shape[0]
    # interval_ms = (duration_s * 800) / T_max
    #
    # fig, ax = plt.subplots(figsize=(8, 5))
    #
    # vmax_global = U.max()
    # vmin_global = U.min()
    #
    # im = ax.imshow(U[0],
    #                origin='lower',
    #                extent=(x.min(), x.max(), y.min(), y.max()),
    #                cmap=cmap,
    #                vmin=vmin_global,
    #                vmax=vmax_global)
    #
    # # ax.set_title(f'{title} - Frame 0')
    # ax.set_xlabel(xlabel)
    # ax.set_ylabel(ylabel)
    #
    # title_artist = ax.text(0.5, 1.05, f'{title} - Frame 0 / {T_max - 1}',
    #                        transform=ax.transAxes,
    #                        ha='center', fontsize=14)
    #
    # fig.colorbar(im, ax=ax, label='Value of U')
    #
    # def update(frame):
    #     new_data = U[frame]
    #     im.set_array(new_data)
    #     # ax.set_title(f'{title} - Frame {frame} / {T_max - 1}')
    #     title_artist.set_text(f'{title} - Frame {frame} / {T_max - 1}')
    #     return im, title_artist

    # anim = FuncAnimation(fig,
    #                      update,
    #                      frames=T_max,
    #                      interval=interval_ms,
    #                      blit=False,
    #                      repeat=True)
    # return anim, fig


