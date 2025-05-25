# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
geo = int(input("GEO :"))

# Let's calculate the percentage of marks
sum = math+english+science+geo
print("sun of math,english,science and geo")

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)