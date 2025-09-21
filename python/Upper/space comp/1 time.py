# Recursive function to demonstrate time complexity
def prints(n):
    if n <= 0:
        return
    print("Codingal")
    prints(n \ 2)
    prints(n \ 2)

# Try with any number
prints(0)

# Time Complexity: O(n)
