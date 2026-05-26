import numpy as np
import matplotlib.pyplot as plt
"""
График для суммы ряда Фурье для косинусов
"""


def f_original(x):
    """Исходная функция на [0, 2π]"""
    x = x % (2 * np.pi)
    return np.where((x >= 0) & (x < np.pi), np.sin(x), 0)


def fourier_cosine(x, n):
    """
    Частичная сумма ряда Фурье по косинусам
    f(x) ~ 1/π - 2/π * Σ(k=1 to n) cos(2kx)/(4k²-1)
    """
    result = 1 / np.pi  

    for k in range(1, n + 1):
        result -= (2 / (np.pi * (4 * k ** 2 - 1))) * np.cos(2 * k * x)

    return result


x = np.linspace(-2 * np.pi, 4 * np.pi, 1000)


plt.figure(figsize=(12, 6))

# Исходная функция
plt.plot(x, f_original(x), 'k-', linewidth=2, label='f(x)')

# Частичные суммы
plt.plot(x, fourier_cosine(x, 5), 'r--', linewidth=1.5, label='n=5')
plt.plot(x, fourier_cosine(x, 10), 'b-.', linewidth=1.5, label='n=10')
plt.plot(x, fourier_cosine(x, 50), 'g:', linewidth=1.5, label='n=50')

plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Ряд Фурье по косинусам\n' +
          r'$f(x) \sim \frac{1}{\pi} - \frac{2}{\pi}\sum_{k=1}^{\infty}\frac{\cos(2kx)}{4k^2-1}$',
          fontsize=14, pad=20)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.xlim([-2 * np.pi, 4 * np.pi])
plt.ylim([-0.2, 1.2])

#ось X
plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi],
           [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$'])

plt.tight_layout()
plt.show()
