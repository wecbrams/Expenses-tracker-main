s1={'A', 'B','C','D', 'E'}
S2={'B','D','V','X','Y','Z'}

uni= s1.union(S2)
total_g=list(uni)

print("The total guest: ", len(total_g))
print("Guest list:\n",total_g)

unio= s1.intersection(S2)
total_g=list(unio)

print("The total guest2: ", len(total_g))
print("Guest list Intersection:\n",total_g)