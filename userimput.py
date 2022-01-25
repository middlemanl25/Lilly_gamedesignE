#lilly middleman
#01/21/22

#we are going to learn the input() function,
#  type casting, branching, looping
import os, random
os.system('cls')
#declare variable for user input
print("guess a number from 1-10: ", end="")
userInfo=int(input()) #input returns a string we must type cast if we need a number
print("the number is %.2f"%(userInfo/3))
guess=int(input("please give me a number"))

#guess a number
#myNumber = 9 instead of using a fixed number we will use random
myNumber=random.randint(1,10)
print("############################################")

print("#                   guess a number         #")
userGuess=int(input("guess a number from 1-10"))
if myNumber ==userGuess:
    print("You guessed it!")
    GameOn=False
while(GameOn):
else:
    print("good luck next time")
print("the number to guess was "+ str(myNumber))
 