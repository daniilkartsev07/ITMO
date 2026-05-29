import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('fourier_graphs', exist_ok=True)



def f_original(x):
    x_mod = np.mod(x, 2 * np.pi)
    return np.where((x_mod >= 0) & (x_mod < np.pi), np.sin(x_mod), 0)



def fourier_general(x, N):
    result = 1 / np.pi + 0.5 * np.sin(x)
    for k in range(1, N + 1):
        result -= (2 / (np.pi * (4 * k ** 2 - 1))) * np.cos(2 * k * x)
    return result


def fourier_cosine(x, N):
    result = 1 / np.pi
    for k in range(1, N + 1):
        result -= (2 / (np.pi * (4 * k ** 2 - 1))) * np.cos(2 * k * x)
    return result



def fourier_sine(x, N):
    return 0.5 * np.sin(x)



x_plot = np.linspace(-2 * np.pi, 4 * np.pi, 2000)
N_values = [5, 10, 50]
colors = {'general': 'blue', 'cosine': 'green', 'sine': 'red'}
linestyles = {5: '--', 10: '-.', 50: ':'}



def plot_fourier(series_func, series_name, title, filename):
    plt.figure(figsize=(12, 6))


    plt.plot(x_plot, f_original(x_plot), 'k-', linewidth=2.5, label='f(x)')


    for N in N_values:
        plt.plot(x_plot, series_func(x_plot, N),
                 color=colors[series_name],
                 linestyle=linestyles[N],
                 linewidth=1.5,
                 label=f'N={N}',
                 alpha=0.8)

    plt.title(title, fontsize=14, pad=15)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x)', fontsize=12)
    plt.legend(loc='upper right', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='gray', linewidth=0.5)
    plt.axvline(x=0, color='gray', linewidth=0.5)
    plt.xlim([-2 * np.pi, 4 * np.pi])
    plt.ylim([-0.2, 1.2])
    plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi],
               [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$'])
    plt.tight_layout()


    filepath = os.path.join('fourier_graphs', filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.show()



plot_fourier(
    fourier_general,
    'general',
    'Общий тригонометрический ряд Фурье',
    'general_series.png'
)

plot_fourier(
    fourier_cosine,
    'cosine',
    'Ряд Фурье по косинусам (чётное продолжение)',
    'cosine_series.png'
)

plot_fourier(
    fourier_sine,
    'sine',
    'Ряд Фурье по синусам (нечётное продолжение)',
    'sine_series.png'
)
