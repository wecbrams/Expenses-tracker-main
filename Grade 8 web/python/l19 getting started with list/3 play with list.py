L = [4,5,1,3,7,10,8,2]
print("The original list\n",L)

count=0

# Finding the sum
for i in L:
    count += i
avg = count/len(L)
print("Sum = ",count)
print("Average = ",avg)

L.sort()
print("Sorted list\n",L)
print("Smallest element is: ",L[0])
print("Largest element is: ",L[-1])

