import numpy as np
import matplotlib.pyplot as plt
"""
График суммы общего тригонометрического ряда Фурье
"""
def S_general(x, n):
    result = 1/np.pi + 1/2*np.sin(x)
    for k in range(1, n+1):
        result -= (2/(np.pi*(4*k**2-1)))*np.cos(2*k*x)
    return result

x = np.linspace(-2*np.pi, 4*np.pi, 1000)

plt.figure(figsize=(10, 6))
plt.plot(x, S_general(x, 5), 'r--', label='n=5')
plt.plot(x, S_general(x, 10), 'b-.', label='n=10')
plt.plot(x, S_general(x, 50), 'g:', label='n=50')
plt.legend()
plt.grid(True)
plt.show()
