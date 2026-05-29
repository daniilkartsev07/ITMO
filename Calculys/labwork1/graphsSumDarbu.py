import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('lab1_graphs', exist_ok=True)

def f(x):
    return np.sin(x)

def plot_darboux(n):
    x_nodes = np.linspace(0, np.pi, n+1)
    f_min, f_max = [], []
    for i in range(n):
        xl, xr = x_nodes[i], x_nodes[i+1]
        if xr <= np.pi/2:
            f_min.append(f(xl)); f_max.append(f(xr))
        elif xl >= np.pi/2:
            f_min.append(f(xr)); f_max.append(f(xl))
        else:
            f_min.append(min(f(xl), f(xr))); f_max.append(1.0)

    plt.figure(figsize=(8, 5))
    plt.plot(np.linspace(0, np.pi, 500), f(np.linspace(0, np.pi, 500)), 'k-', linewidth=2, label='f(x)')
    plt.step(x_nodes, [0] + f_min, where='post', color='blue', alpha=0.5, label='Нижняя сумма')
    plt.step(x_nodes, [0] + f_max, where='post', color='red', alpha=0.5, label='Верхняя сумма')
    plt.title(f'Суммы Дарбу, n={n}')
    plt.legend(); plt.grid(True, alpha=0.3)
    plt.xlim([0, np.pi]); plt.ylim([0, 1.2])
    plt.tight_layout()
    plt.savefig(f'lab1_graphs/darboux_n{n}.png', dpi=300)
    plt.show()

def plot_riemann(n):
    np.random.seed(42)
    x_nodes = np.linspace(0, np.pi, n+1)
    dx = np.pi / n
    plt.figure(figsize=(8, 5))
    plt.plot(np.linspace(0, np.pi, 500), f(np.linspace(0, np.pi, 500)), 'k-', linewidth=2, label='f(x)')
    for i in range(n):
        xi = np.random.uniform(x_nodes[i], x_nodes[i+1])
        rect = plt.Rectangle((x_nodes[i], 0), dx, f(xi), facecolor='skyblue', edgecolor='blue', alpha=0.5)
        plt.gca().add_patch(rect)
    plt.title(f'Интегральная сумма (случайная), n={n}')
    plt.legend(); plt.grid(True, alpha=0.3)
    plt.xlim([0, np.pi]); plt.ylim([0, 1.2])
    plt.tight_layout()
    plt.savefig(f'lab1_graphs/riemann_n{n}.png', dpi=300)
    plt.show()


for n in [5, 10, 100]:
    plot_darboux(n)
    plot_riemann(n)

