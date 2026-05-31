import numpy as np
import matplotlib.pyplot as plt

# Исходная функция на периоде [0, 2pi]
def f_original(x):
    x_mod = np.mod(x, 2 * np.pi)
    return np.where((x_mod >= 0) & (x_mod < np.pi), np.sin(x_mod), 0.0)

# Сумма общего тригонометрического ряда Фурье 
def fourier_general(x, N):
    res = np.full_like(x, 1.0 / np.pi)
    res += 0.5 * np.sin(x)  
    for n in range(2, N + 1):
        if n % 2 == 0: 
            k = n // 2
            a_2k = -2.0 / (np.pi * (4 * k**2 - 1))
            res += a_2k * np.cos(n * x)
    return res

# Сумма ряда по косинусам
def fourier_cos(x, N):
    res = np.full_like(x, 1.0 / np.pi)
    for n in range(1, N + 1):
        if n % 2 == 0:  
            k = n // 2
            a_2k = -2.0 / (np.pi * (4 * k**2 - 1))
            res += a_2k * np.cos(n * x)
    return res

# Сумма ряда по синусам 
def fourier_sin(x):
    return 0.5 * np.sin(x)

# Настройка сетки точек 
x_plot = np.linspace(-2 * np.pi, 4 * np.pi, 1000)
N_terms = 30 

plt.figure(figsize=(12, 10))

#Общий тригонометрический ряд
plt.subplot(3, 1, 1)
plt.plot(x_plot, f_original(x_plot), label='Исходная $f(x)$', color='gray', linestyle='--', alpha=0.7)
plt.plot(x_plot, fourier_general(x_plot, N_terms), label=f'Сумма общего ряда (N={N_terms})', color='blue', lw=2)
plt.title('1. График суммы общего тригонометрического ряда Фурье')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)

#Ряд по косинусам
plt.subplot(3, 1, 2)
f_even_visual = f_original(np.abs(x_plot))  
plt.plot(x_plot, f_even_visual, label='Четное продолжение $f(x)$', color='gray', linestyle='--', alpha=0.7)
plt.plot(x_plot, fourier_cos(x_plot, N_terms), label=f'Сумма ряда по косинусам (N={N_terms})', color='green', lw=2)
plt.title('2. График суммы ряда Фурье по косинусам (Четное продолжение)')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
#Ряд по синусам
plt.subplot(3, 1, 3)
f_odd_visual = np.sign(x_plot) * f_original(np.abs(x_plot))  
plt.plot(x_plot, f_odd_visual, label='Нечетное продолжение $f(x)$', color='gray', linestyle='--', alpha=0.7)
plt.plot(x_plot, fourier_sin(x_plot), label='Сумма ряда по синусам (только $b_1$)', color='red', lw=2)
plt.title('3. График суммы ряда Фурье по синусам (Нечетное продолжение)')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)

plt.tight_layout()
plt.show()
