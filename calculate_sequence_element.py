import math
def sequence_a(x, n):
    for k in range(n + 1):
        yield x**k / math.factorial(k)
for value in sequence_a(2, 5):
    print(f"b = {value}")


