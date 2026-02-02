print("Select your ride:\n1. Bike \n2. Car ")

#select your ride
choice = int( input("Enter your choice: ") )


if( choice == 1 ): 
  print( "what type of bike? " )
  print("1.Scooty\n")
  print("2.Scooter\n")

  choice2=int(input("Enter you choice2: "))
  if choice2==1:
    print("you have selected scooty")
  elif choice2 ==2:
    print("you have selected scooter")
  else:
    print("Invalid Choice")
    

elif( choice == 2 ): 
  print( "what type of car?" )
  print("1.Sedan")
  print("2.XUV")
  choice3=int(input("enter your choice3: "))

  if choice3==1: 
    print("you have selected sedan")
  elif choice3 ==2:
    print("you have selected XUV")
  else:
    print("Invalid Choice")

else: #outer else statement
  print("Wrong choice!")