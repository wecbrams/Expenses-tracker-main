def fun1(n):
  return n*(n+1)/2  # (4*5)\2
    # takes constant time and space O(1)
print(fun1(4))

def fun2(n):
    sum = 0
    for i in range(1, n+1): # 1+2+3+4
        sum += i
        # linear time complexity O(n)
        # O(1) Space

print(fun2(4))

# 1 + (1+1) + (1+1+1) + (1+1+1+1)
def fun3(n):
    sum = 0
    for i in range(1, n+1):
      for j in range(i, i+1):
        sum += 1
      return sum
print(fun3(4))
      
  
  