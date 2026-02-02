# 200 100 50 20
amount=int(input("Please enter the amount to withdraw: "))

note_1 = amount //200
note_2 = (amount%200) //100
note_3 = ((amount%200)%100) //50
note_4 = (((amount%200)%100)%50) //20

print("Notes of 200 Dirhams is ", note_1)
print("Notes of 100 Dirhams is ", note_2)
print("Notes of 50 Dirhams is ", note_3)
print("Notes of 20 Dirhams is ", note_4)
