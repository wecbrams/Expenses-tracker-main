def fibonacci(n):
    a, b = 0, 1
    series = [a]
    for _ in range(1, n):
        a, b = b, a + b
        series.append(a)
    return series

n = 10  # testing
print(f"Fibonacci Series up to {n} terms: {fibonacci(n)}")
