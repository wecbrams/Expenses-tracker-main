import math

def printPowerset(set, setsize):
    powerSetsize = int(math.pow(2, setsize))
    for outer in range(0, powerSetsize):
        for inner in range(0, setsize):
            if (outer & (1 << inner)) > 0:
                print(set[inner], end=" ")
        print()
size = int(input("Enter array size: "))
set = []
for i in range(0, size):
    n = int(input("Enter element: "))
    set.append(n)
printPowerset(set, len(set))