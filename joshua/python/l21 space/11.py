#Constant space
def sum_n(n):
    return n * (n + 1) // 2  # integer result
print("Sum of first n numbers (n=5):", sum_n(5))

#linear space
def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total

# Examples
a = [12, 3, 4, 15]
print("Array sum:", array_sum(a))
