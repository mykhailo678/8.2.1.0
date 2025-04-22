def harmonic_sum(n):
    total = 0
    for k in range(1, n + 1):
        total += 1 / k
        yield total  # Проміжна сума

# Приклад:
for partial_sum in harmonic_sum(5):
    print(f"Partial sum: {partial_sum}")

