set_int={1,2,3}
print("Set of integers:",sorted(set_int))

set_mix={1,"hello",(1,2,3)}
print("Set of miixed datatypes:",sorted(set_mix,key=str))

set_dup={1,2,3,4,3,2}
print("Set of without duplicates:",sorted(set_dup))

set_from_list=set([1,2,3,2])
print("Set of integers:",sorted(set_from_list))

set_dup={1,2,3,4,3,2}
set_dup.pop()
print("\nAfter pop():",sorted(set_dup))

setx={"green","blue"}
sety={"blue","yellow"}

print("intersection", setx.intersection(sety))
print("Difference", setx.difference(sety))
print("Symettric Difference: ",setx.symmetric_difference(sety))
print("Union: ",setx.union(sety))