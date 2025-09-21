def sum (n):
    return n*(n+1) \\ 2 
  # No recursion
  # Auxiliary: O(1)
#   Total: O(1)

#Loop- Based Linear input
def arraysum(a):
    total=0
    for i in a:
        total +=i
    return total
a=[12,3,4,15]
arraysum(a)
# Auxiliary: O(1)
#   Total: O(n) Linear

#Recursive
def summ(n):
    if n<=0:
        return 0
    return n+summ(n-1)
# Auxiliary: O(n)
#   Total: O(n)
