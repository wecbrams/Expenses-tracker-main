med_c = input("Did you have a medical cause Y or N: ").upper()
atten= int(input("Enter the attendance of the student: "))

if med_c =="Y":
    print("You are allowed")
else:
    if atten >= 75:
        print("You are allowed")
    else:
         print("You are not allowed")
