import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x_sym = sp.Symbol('x')
f_sym = x_sym
l_val = np.pi
N_terms = 10

def get_fourier_series(f, l, N, mode='general'):
    x = sp.Symbol('x')
    a0, a_coeffs, b_coeffs = 0, [], []

    if mode == 'general':
        a0 = (1 / l) * sp.integrate(f, (x, -l, l))
        for n in range(1, N + 1):
            an = (1 / l) * sp.integrate(f * sp.cos(n * sp.pi * x / l), (x, -l, l))
            bn = (1 / l) * sp.integrate(f * sp.sin(n * sp.pi * x / l), (x, -l, l))
            a_coeffs.append(an)
            b_coeffs.append(bn)
    elif mode == 'even':  # Только косинусы
        a0 = (2 / l) * sp.integrate(f, (x, 0, l))
        for n in range(1, N + 1):
            an = (2 / l) * sp.integrate(f * sp.cos(n * sp.pi * x / l), (x, 0, l))
            a_coeffs.append(an)
            b_coeffs.append(0)
    elif mode == 'odd':  # Только синусы
        a0 = 0
        for n in range(1, N + 1):
            bn = (2 / l) * sp.integrate(f * sp.sin(n * sp.pi * x / l), (x, 0, l))
            a_coeffs.append(0)
            b_coeffs.append(bn)


    def fourier_sum(x_arr):
        res = float(a0) / 2
        for n in range(1, N + 1):
            if mode != 'odd':
                res += float(a_coeffs[n - 1]) * np.cos(n * np.pi * x_arr / l)
            if mode != 'even':
                res += float(b_coeffs[n - 1]) * np.sin(n * np.pi * x_arr / l)
        return res

    return fourier_sum



x_plot = np.linspace(-3 * float(l_val), 3 * float(l_val), 1000)


s_general = get_fourier_series(f_sym, l_val, N_terms, 'general')
s_even = get_fourier_series(f_sym, l_val, N_terms, 'even')
s_odd = get_fourier_series(f_sym, l_val, N_terms, 'odd')


plt.figure(figsize=(12, 10))

# График 1: Общий ряд
plt.subplot(3, 1, 1)
plt.plot(x_plot, s_general(x_plot), label=f'Сумма общего ряда (N={N_terms})', color='blue')
plt.axvline(x=0, color='gray', linestyle='--')
plt.title('1. Общий тригонометрический ряд Фурье')
plt.grid(True)
plt.legend()

# График 2: Четное продолжение
plt.subplot(3, 1, 2)
plt.plot(x_plot, s_even(x_plot), label=f'Ряд по косинусам (N={N_terms})', color='green')
plt.axvline(x=0, color='gray', linestyle='--')
plt.title('2. Четное продолжение (Ряд по косинусам)')
plt.grid(True)
plt.legend()

# График 3: Нечетное продолжение
plt.subplot(3, 1, 3)
plt.plot(x_plot, s_odd(x_plot), label=f'Ряд по синусам (N={N_terms})', color='red')
plt.axvline(x=0, color='gray', linestyle='--')
plt.title('3. Нечетное продолжение (Ряд по синусам)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
