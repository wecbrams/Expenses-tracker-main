height =float(input("Enter height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight/(height/100)**2

print("Your BMI is",BMI)
if BMI <= 18.4:
    print("You ar under weight")
elif BMI <=24.9:
    print("You are healthy")
elif BMI <= 34.9:
    print("You're over weight")
elif BMI <=39.9:
    print("You're obese")
else:
    print("You're severely obese")

