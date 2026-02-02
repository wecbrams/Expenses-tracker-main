import math
def printPowerset(set, Setsize):
    powerSetSize=(int)(math.pow(2,Setsize))
    for outer in range(0, powerSetSize):
        for inner in range(0, Setsize):
            if(outer & (1<<inner))>0:
                print(set[inner], end=" ")
        print()
size = int(input("Enter the size: "))
set=[]
for i in range(0, size):
    n=int(input("Enter element"))
    set.append(n)
printPowerset(set, len(set))