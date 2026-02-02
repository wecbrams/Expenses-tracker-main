def swap(a, b): #XOR
  a = a ^ b  
  b = a ^ b
  a = a ^ b
  print("After swapping: a =", a, "and b =", b)
  """
  a = 10 = 1010
  b = 20 = 10100

  a = 10^20 
  a= 01010 ^ 10100= 11110=30 

  b = 30 ^ 20
  b= 11110 ^ 10100= 01010=10

  a = 30 ^ 10
  a= 11110 ^ 01010= 10100=20
  """

def swap2(a, b): 
  a = (a & b) + (a | b)
  b = a + (~b) + 1
  a = a + (~b) + 1
  print("After swapping: a =", a, "and b =", b)

swap(10, 20)
swap2(10, 20)
