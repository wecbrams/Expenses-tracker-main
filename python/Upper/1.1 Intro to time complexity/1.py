def fun1(n):
    return n*(n+1)/2  # Constant O(1)
print(fun1(4))

def fun2(n):
    sum=0
    for i in range(1, n+1): # Linear O(n)
        sum+=i
    return sum
print("Function2\n",fun2(4))

def fun3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):  #Quodratic O(n2)
            sum+1
    return sum
print("Function 3\n",fun3(4))