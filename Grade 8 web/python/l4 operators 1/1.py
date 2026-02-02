tree1 =98
tree2=94
tree3=41
tree4=95
tree5 = 11

sum = tree1+tree2+tree3+tree4+tree5
print("The sum of all 5 trees is: ",sum)

average=sum/5
print("The average of all 5 trees is: ",average)

amount=int(input("Enter the amount to withdraw: "))
note_1 = amount//200
note_2 = (amount%200)//100
note_3 = ((amount%200)%100)//50

print("Notes for 200 GHS",note_1)
print("Notes for 100 GHS",note_2)
print("Notes for 50 GHS",note_3)

print("Enter the marks obtained in 4 subjects:\n")
math= int(input("Math: "))
english= int(input("English: "))
science= int(input("Science: "))
chemistry= int(input("Chemistry: "))

sum=math+english+science+chemistry

perc=(sum/400)*100
print("Percentage marks = ",perc)