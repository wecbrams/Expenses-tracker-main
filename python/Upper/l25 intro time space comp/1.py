def fun1(n):
  return n*(n+1)/2 # Constant time complexity O(1)
print(fun1(4))

def fun2(n):
    sum = 0
    for i in range(1, n+1): #Linear time complexity O(n)
        sum += i
    return sum

def fun3(n):
    sum = 0
    for i in range(1, n+1):
      for j in range(i, n+1): #Around n²\2 steps → Time Complexity = O(n²) (Quadratic time)
        sum += 1
      return sum
      
      
  
  