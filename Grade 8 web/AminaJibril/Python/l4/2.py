# Activity 2 Count of notes
Amount=int(input("Enter Amount for withdraw: "))
note_1 = Amount//1000
note_2 = (Amount%1000)//500
note_3 = ((Amount%1000)%500)//200
note_4 =  (((Amount%1000)%500)%200)//100
note_5 =  ((((Amount%1000)%500)%200)%100)//50

print("Notes of 1000 Kenya Shillings",note_1)
print("Notes of 500 Kenya Shillings",note_2)
print("Notes of 200 Kenya Shillings",note_3)
print("Notes of 100 Kenya Shillings",note_4)
print("Notes of 50 Kenya Shillings",note_5)

# Assigniment operators
# += 
num = 9
num+=7

print(num)