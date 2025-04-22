import numpy as np

def determinant_generator(n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i][i] = 5
        if i > 0:
            A[i][i - 1] = 2
        if i < n - 1:
            A[i][i + 1] = 3
    yield np.linalg.det(A)  # Лише одне значення, але через yield

# Приклад:
for det in determinant_generator(4):
    print(f"Determinant: {det}")
