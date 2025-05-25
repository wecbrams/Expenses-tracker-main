import math

def printPowerSet(set, SetSize):
    PowerSetSize = int(math.pow(2, SetSize))
    for outer in range(0, PowerSetSize):
        for inner in range(0, SetSize): 
            if (outer & (1 << inner)) > 0:
                print(set[inner], end=" ")
        print("")
size = int(input("Enter array size: "))
set = []
for i in range(0, size):
    n = int(input(f"Enter element {i + 1}: "))
    set.append(n)
print("Power set of the given set is:")
printPowerSet(set, len(set))
