#lillymiddleman

import random, os
os.system('cls')

#today we are learning try and except, funtions, elif

#lets make menu a function key work def
def menu():
    print('##################################################')
    print('#             Guess A Number Menu                 #')
    print('#                                                 #')
    print('#              1. Choices 1-10                    #')
    print('#              2. Choices 1-50                    #') 
    print('#              3. Choices 1-100                   #')
    print('#                   select your choice            #')
    print('##################################################')
#checking for correct user input

menu()
check=True
while check:
    try:
        choice=int(input("choice:  "))
        check= False
    except ValueError:
        print("sorry wrong choice, please enter 1 to 3 only")

if choice == 1:
    myNumber= random.randint(1,10)
elif choice == 2:
     myNumber= random.randint(1,50)
elif choice == 3:
    myNumber= random.randint(1,100)
print(choice)
GameOn=True
while(GameOn):
    userguess=int(input("give me a number"))
    if myNumber ==userGuess:
        print("you guessed it!")
        GameOn=False
    else:
        print("good luck next time", myNumber)
        print("the number to guess was " + str(myNumber))
        os.sytem('cls')
        menu()