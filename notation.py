# def printnumber(n):
#   literation = 0
#   print("the total number entered my user is",n)
#   literation+=1
#   print("total literation done by computer is",literation,"\n")
# printnumber(10)
# printnumber(200)
# print("\n with any 'n' the time taken by the computer will not change")

# def OnTime(n):
#   iteration=0
#   for i in range(1,n+1):
#     iteration+=1
#   print("When n is ",n," Iterations = ",iteration)

# OnTime(10)
# OnTime(20)
# OnTime(42)

# print("\nWith every 'n' the time taken and iterations will increase linearly")

def test(n):
  iteration = 0
  for i in range(0,n): #  outer loop: runs n times
    for j in range(0,n): # inner loop: runs n times
      print("*",end="")
      iteration+=1
    print("") # Moves to next line
  print("\nwhen n is",n,"iteration =",iteration)
test(5)
test(4)
test(3)

print("\n with every 'n' the taken = n^2")
print("(n^2)")