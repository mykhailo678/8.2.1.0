def exp_taylor(x, epsilon):
    term = 1
    sum_ = term
    k = 1
    yield sum_
    while abs(term) >= epsilon:
        term *= x / k
        sum_ += term
        k += 1
        yield sum_
for approx in exp_taylor(2, 1e-6):
    print(f"Approximation: {approx}")
