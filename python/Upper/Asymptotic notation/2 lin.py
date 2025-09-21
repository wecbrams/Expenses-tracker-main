def OnTime(n): # Linear time complexity O(n)
    for i in range(1, n + 1):
        print("Iteration:", i)
    print("Total iterations done:", n, "\n")

# Try different inputs
OnTime(5)
OnTime(10)
OnTime(20)
