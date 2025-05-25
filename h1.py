# # Initialize dictionary
# test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
  
# # printing original dictionary
# print("The original dictionary : " +  str(test_dict))
  
# # Initialize value 
# K = 2
  
# # Using loop
# # Selective key values in dictionary
# res = 0
# for key in test_dict:
#     if test_dict[key] == K:
#         res = res + 1
      
# # printing result 
# print("Frequency of K is : " + str(res))

# print("What is the type of above given database -\n 1)Relational Database \n 2)Non-Relational Database")
# answer = int(input("Enter your guess here..."))
# if answer == 2:
#   print("You guessed it right!")
# else:
#   print("Unfortunately your guess was wrong.")

# print("\nPlease tell your mentor why you guessed this?")
print("What is the type of above given database -\n 1)Relational Database \n 2)Non-Relational Database")
answer = int(input("Enter your guess here..."))
if answer == 1:
  print("You guessed it right!")
else:
  print("Unfortunately your guess was wrong.")

print("\nPlease tell your mentor why you guessed this?")