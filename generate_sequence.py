def product_sequence(n):
    a = [1, 1, 3]
    product = 1
    for i in range(3):
        product *= 3 * a[i]
        yield product
    for k in range(3, n + 1):
        next_a = (a[k - 3] + a[k - 2]) / (2 * k - 1)
        a.append(next_a)
        product *= 3 * next_a
        yield product

for p in product_sequence(5):
    print(f"Product step: {p}")
