import math

"""
АЛГОРИТМ ГРАМА-ШМИДТА 
"""



def dot_product(v1, v2):
    """Скалярное произведение векторов"""
    if len(v1) != len(v2):
        raise ValueError("Векторы должны иметь одинаковую размерность")
    return sum(a * b for a, b in zip(v1, v2))

def vector_norm(v):
    """Евклидова норма (длина) вектора"""
    return math.sqrt(dot_product(v, v))

def vector_subtract(v1, v2):
    """Вычитание векторов"""
    if len(v1) != len(v2):
        raise ValueError("Векторы должны иметь одинаковую размерность")
    return [a - b for a, b in zip(v1, v2)]

def scalar_mult(scalar, v):
    """Умножение вектора на скаляр"""
    return [scalar * x for x in v]

def normalize(v, tol=1e-10):
    """Нормализация вектора (деление на длину)"""
    norm = vector_norm(v)
    if norm < tol:
        raise ValueError("Нельзя нормализовать нулевой вектор")
    return [x / norm for x in v]

def gram_schmidt(vectors, normalize_result=True, tol=1e-10):

    """
    Алгоритм ортогонализации Грама-Шмидта
    """
    orthogonal = []

    print(f"\nКоличество входных векторов: {len(vectors)}")
    print(f"Размерность пространства: {len(vectors[0]) if vectors else 0}")

    for i, v in enumerate(vectors):
        u = v[:]
        for j, orth_v in enumerate(orthogonal):
            dot_u_orth = dot_product(u, orth_v)
            dot_orth_orth = dot_product(orth_v, orth_v)

            if abs(dot_orth_orth) > tol:
                proj_coeff = dot_u_orth / dot_orth_orth
                proj = scalar_mult(proj_coeff, orth_v)
                u = vector_subtract(u, proj)

        u_norm = vector_norm(u)
        if u_norm > tol:
            orthogonal.append(u)
            print(f"Вектор {i + 1}: добавлен (норма = {u_norm:.4f})")
        else:
            print(f"Вектор {i + 1}: отклонен (линейно зависим)")

    if normalize_result:
        print("\nНормализация векторов")
        orthonormal = []
        for i, v in enumerate(orthogonal):
            v_normalized = normalize(v, tol)
            orthonormal.append(v_normalized)
            print(f"Вектор {i + 1}: норма после нормализации = {vector_norm(v_normalized):.10f}")
        return orthonormal
    else:
        return orthogonal

def print_vectors(vectors, title="Векторы"):
    print(f"\n{title}:")
    for i, v in enumerate(vectors):
        print(f"  v{i + 1} = {[f'{x:.4f}' if isinstance(x, float) else x for x in v]}")

def check_orthonormality(vectors, tol=1e-10):
    print("\nПроверка ортонормированности:")
    n = len(vectors)
    is_orthonormal = True
    for i in range(n):
        for j in range(n):
            dot = dot_product(vectors[i], vectors[j])
            if i == j:
                if abs(dot - 1.0) > tol:
                    print(f"||e{i + 1}||² = {dot:.10f} (ОШИБКА)")
                    is_orthonormal = False
                else:
                    print(f"||e{i + 1}||² = {dot:.10f} ✓")
            else:
                if abs(dot) > tol:
                    print(f"(e{i + 1}, e{j + 1}) = {dot:.10f} (ОШИБКА)")
                    is_orthonormal = False
                else:
                    print(f"(e{i + 1}, e{j + 1}) = {dot:.10f} ✓")
    return is_orthonormal



A = [
    [3, 0, 0],
    [0, -1, 0],
    [0, 0, 2]
]

print("Исходная матрица A:")
for row in A:
    print(row)


input_vectors = [
    [3, 0, 0],
    [0, -1, 0],
    [0, 0, 2]
]


orthonormal_basis = gram_schmidt(input_vectors, normalize_result=True)

print_vectors(orthonormal_basis, "Итоговый ортонормированный базис")
