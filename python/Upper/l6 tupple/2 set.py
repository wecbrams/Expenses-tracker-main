setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)
setc = setx.union(sety)
print("\nUnion of above sets:")
print(setc)
setd = setx.difference(sety)
print("\nDifferent of above sets:")
print(setc)

setc = setx.symmetric_difference(sety)
print("\nsymmetric_difference of above sets:")
print(setc)


