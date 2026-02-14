l = [4,5,1,2,9,10,8,7]
count = 0
for i in l:
    count +=1
avg= count/len(l)
print(f"The sum = {count}")
print(f"The Average = {avg}")

l.sort()
print(f("Smallest Element is ",l[0]))
print(f("Largest Element is ",l[-1]))
