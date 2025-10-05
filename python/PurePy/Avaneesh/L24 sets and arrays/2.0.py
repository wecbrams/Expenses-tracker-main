setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)

print("The difference: ",setx.difference(sety))

print("The symmetric_difference: ",setx.symmetric_difference(sety))
print("The union: ",setx.union(sety))

