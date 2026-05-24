import numpy as np

"""
Проверка оператора на ортогональность
"""

A = np.array([
    [3, 0, 0],
    [0, -1, 0],
    [0, 0, 2]
])
AT = A.T
check_matrix = AT @ A

I = np.eye(3)

is_orthogonal = np.allclose(check_matrix, I)

print("Матрица A^T * A:")
print(check_matrix)

print("\nЕдиничная матрица (I):")
print(I)

if is_orthogonal:
    print("Оператор является ортогональным")
else:
    print("Оператор не является ортогональным")
