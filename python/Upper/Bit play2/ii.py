def oddoccuring(arr):
    res=0
    for element in arr:
        res =res^element

    return res
arr=[]
n=int(input("Enter array size: ")) 
while(n):
    num=int(input("Enter a number: "))
    arr.append(num)
    n-=1
print('\nOdd occuring number is: ',oddoccuring(arr))
    