# Example 1: Constant Space Complexity
def sum_n(n):
    return n * (n + 1) // 2

print("Sum using formula:", sum_n(10))
# Space Complexity: O(1)


# Example 2: Iterative - Array Sum (Linear Space due to input)
def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

a = [12, 3, 4, 15]
print("Sum of array:", array_sum(a))
# Auxiliary Space: O(1), Total Space: O(n) because of input array
# Total space= Auxiliary space+input space


# Example 3: Recursive - Sum of first n numbers
def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n-1)

print("Recursive sum:", recursive_sum(5))
# Space Complexity: O(n) due to recursion stack
