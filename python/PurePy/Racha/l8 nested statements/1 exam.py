medical_course= input("Did you have a medical cause Y or N: ").strip().upper()
atten=int(input("Enter the attendance of the student: "))
if medical_course=='Y':
   print("The student is allowed to sit in the exam")

elif medical_course=='N':
    if atten>=75:
         print("The student is allowed to sit in the exam")
    else:
         print("The student is not allowed to sit in the exam")
else:
    print("Invalid input. Please enter Y or N for medical cause.")

medical_course= input("Did you have a medical cause Y or N: ").strip().upper()
if medical_course not in ['Y', 'N']:
    print("Invalid input. Please enter Y or N for medical cause.")
else:
    if medical_course=='Y':
        print("The student is allowed to sit in the exam")
    else:
        atten=int(input("Enter the attendance of the student: "))
        if atten>=75:
            print("The student is allowed to sit in the exam")
        else:
            print("The student is not allowed to sit in the exam")