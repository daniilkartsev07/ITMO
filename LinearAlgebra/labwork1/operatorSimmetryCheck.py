import numpy as np

"""
Проверка оператора на симметричность
"""

A = np.array([
    [3, 0, 0],
    [0, -1, 0],
    [0, 0, 2]
])

# Транспонируем матрицу A
AT = A.T

# Проверяем условие A^T == A
is_symmetric = np.allclose(AT, A)

print("Матрица A:")
print(A)

print("\nТранспонированная матрица A^T:")
print(AT)

if is_symmetric:
    print("\nОператор является симметрическим (A^T = A)")
else:
    print("\nОператор не является симметрическим (A^T != A)")
