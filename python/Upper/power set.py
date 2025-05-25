ourset = ['a', 'b', 'c']  # Example set
SetSize = len(ourset)
PowerSetSize = 1 << SetSize  # 2^n

# Generate all subsets
for counter in range(PowerSetSize):
    for j in range(SetSize):
        # Check if j-th bit in counter is set
        if counter & (1 << j):
            print(ourset[j], end="")
    print()
