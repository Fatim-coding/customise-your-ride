print("select your ride: ")
print("1. Bike")
print("2. car")

#take input of number 1 or 2
#select your ride
choice = int( input("Enter your choice: "))

#user entering option 2
if( choice == 2): #condition 2 outer if statement
    print("what type of car? " )
    print("1.tesla\n")
    print("2.Audi\n")

#condition for selecting the type of car
choice2=int(input("Enter you choice2: "))
if choice2==1: #inner if statement
    print("you have selected car")
else:
    print("you have selected car")
#User entering option 2
elif( choice == 2 ): #outer elif statement
    print("what type of car" )
    print("1.tesla")
    print("2.Audi")
    choice3=int(input("Enter your choice3: "))

if choice3==2: #inner if statement
#condition for selecting the type of car
     print("you have selected tesla")
else:
    print("you have selected Audi")

else: #outer else statement
     print("Wrong choice!")