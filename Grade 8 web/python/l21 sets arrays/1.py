myset={1,2,3}
print(myset)

myset={1.0,"Hello",(1,2,3)}
print(myset)
myset=set([1,2,3,4,5,2,1])
print(myset)

myset.pop()
print("After removing an item from a set")
print(myset)

setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)

print("Difference \n",setx.difference(sety))
print("symmetric difference\n",setx.symmetric_difference(sety))
print("union\n",setx.union(sety))