def OnTime(n):
    for i in range(1, n + 1):
        print("Iteration:", i)
    print("Total iterations done:", n, "\n")

# Try different inputs
# OnTime(5)
# OnTime(10)
# OnTime(20)

# O(n)


def ONSquareTime(n):
    iteration = 0
    for i in range(n): # outer loop
        for j in range(n): # inner loop
            iteration += 1
            print(f"Iteration {iteration}: (i={i}, j={j})")
    print("Total iterations done:", iteration, "\n")

# Try different inputs
ONSquareTime(3)
ONSquareTime(4)
ONSquareTime(5)

# O(n^2)