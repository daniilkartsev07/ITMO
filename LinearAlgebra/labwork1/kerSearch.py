import math
"""
Поиск ядра
"""

A = [
    [3, 0, 0],
    [0, -1, 0],
    [0, 0, 2]
]

print("Матрица A:")
for row in A:
    print(row)

def copy_matrix(M):
    return [row[:] for row in M]


def print_matrix(M, name="Матрица"):
    print(f"{name}:")
    for row in M:
        print([f"{x:.4f}" if isinstance(x, float) else x for x in row])
    print()


def gauss_jordan(M):
    """
    Метод Гаусса для приведения матрицы к приведённому ступенчатому виду
    """
    m = len(M)  
    n = len(M[0])  

    
    matrix = copy_matrix(M)

    
    pivot_row = 0
    pivot_cols = []

    for col in range(n):
        if pivot_row >= m:
            break


        max_row = pivot_row
        for row in range(pivot_row + 1, m):
            if abs(matrix[row][col]) > abs(matrix[max_row][col]):
                max_row = row


        if abs(matrix[max_row][col]) < 1e-10:
            continue


        matrix[pivot_row], matrix[max_row] = matrix[max_row], matrix[pivot_row]


        pivot_val = matrix[pivot_row][col]
        for j in range(n):
            matrix[pivot_row][j] /= pivot_val


        for row in range(m):
            if row != pivot_row:
                factor = matrix[row][col]
                for j in range(n):
                    matrix[row][j] -= factor * matrix[pivot_row][j]

        pivot_cols.append(col)
        pivot_row += 1

    return matrix, pivot_cols


def find_kernel_basis(A):

    """
    Поиск базиса ядра матрицы A
    """
    m = len(A)
    n = len(A[0])


    rref, pivot_cols = gauss_jordan(A)

    print("Приведённая ступенчатая форма:")
    print_matrix(rref, "RREF")

    print(f"Ведущие столбцы: {pivot_cols}")
    print(f"Ранг матрицы: {len(pivot_cols)}")
    print(f"Размерность ядра: {n - len(pivot_cols)}")


    free_cols = [j for j in range(n) if j not in pivot_cols]
    print(f"Свободные столбцы: {free_cols}")


    if not free_cols:
        return []


    kernel_basis = []

    for free_col in free_cols:
        
        vector = [0] * n
        vector[free_col] = 1

  
        for i, pivot_col in enumerate(pivot_cols):
            vector[pivot_col] = -rref[i][free_col]

        kernel_basis.append(vector)

    return kernel_basis


def vector_norm(v):
    """Евклидова норма вектора"""
    return math.sqrt(sum(x * x for x in v))


def matrix_vector_mult(A, v):
    """Умножение матрицы на вектор"""
    m = len(A)
    n = len(v)
    result = [0] * m
    for i in range(m):
        for j in range(n):
            result[i] += A[i][j] * v[j]
    return result




print("РЕЗУЛЬТАТЫ ПОИСКА ЯДРА")

kernel_basis = find_kernel_basis(A)

if not kernel_basis:
    print("\nЯдро тривиальное: ker A = {0}")
    print("dim(ker A) = 0")
    print("Базис ядра: пустое множество")
else:
    print("\nБазис ядра:")
    for i, vec in enumerate(kernel_basis):
        print(f"  Вектор {i + 1}: {vec}")

    print(f"\ndim(ker A) = {len(kernel_basis)}")


_, pivot_cols = gauss_jordan(A)
rank_A = len(pivot_cols)
n = len(A[0])
defect_A = n - rank_A

print(f"\nРанг матрицы A: {rank_A}")
print(f"Дефект матрицы A: {defect_A}")
print(f"Проверка: rank + defect = {rank_A + defect_A} (должно быть {n})")

print(f"\nIm A = R^{rank_A} (размерность образа = рангу)")
