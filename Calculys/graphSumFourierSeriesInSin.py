import numpy as np
import matplotlib.pyplot as plt
"""
График суммы ряда Фурье для синусов
"""

def f_original(x):
    """Исходная функция на [0, 2π]"""
    x = x % (2 * np.pi)  
    return np.where((x >= 0) & (x < np.pi), np.sin(x), 0)


def fourier_sine(x, n):
    """
    Частичная сумма ряда Фурье по синусам
    f(x) ~ 1/2 * sin(x)

    Примечание: для этой функции все коэффициенты b_n = 0 при n > 1,
    поэтому ряд содержит только один член!
    """
    # Ряд по синусам для данной функции содержит только один член
    return 0.5 * np.sin(x)



x = np.linspace(-2 * np.pi, 4 * np.pi, 1000)


plt.figure(figsize=(12, 6))

# Исходная функция
plt.plot(x, f_original(x), 'k-', linewidth=2, label='f(x)')

# Частичная сумма (для ряда по синусам это просто 1/2*sin(x))
# Показываем одну и ту же кривую для всех n, так как ряд содержит только один член
plt.plot(x, fourier_sine(x, 5), 'r--', linewidth=1.5, label='n=5, 10, 50')

plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Ряд Фурье по синусам\n' +
          r'$f(x) \sim \frac{1}{2}\sin(x)$',
          fontsize=14, pad=20)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.xlim([-2 * np.pi, 4 * np.pi])
plt.ylim([-0.6, 1.1])

#ось X
plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi],
           [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$'])

plt.tight_layout()
plt.show()

# Отдельный график на отрезке [0, 2π]
plt.figure(figsize=(8, 5))
plt.plot(x, f_original(x), 'k-', linewidth=2, label='f(x)', alpha=0.7)
plt.plot(x, fourier_sine(x, 1), 'b-', linewidth=2, label=r'$\frac{1}{2}\sin(x)$')
plt.title('Ряд Фурье по синусам (нечетное продолжение)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim([0, 2 * np.pi])
plt.ylim([-0.6, 1.1])
plt.xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
           ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.tight_layout()
plt.show()
