#lilly middleman

user='paper'
computer = 1

import random, os
os.system('cls')

#guess rock paper or scissors
#paper beats rock, rock beats scissors, and scissors beats paper
def menu():
    print('##################################################')
    print('#             rock paper scissor                  #')
    print('#                                                 #')
    print('#              1. Choice paper                    #')
    print('#              2. Choices rock                    #') 
    print('#              3. Choices scissors                #')
    print('#                   select your choice            #')
    print('##################################################')

GameOn = True
while (GameOn):
    menu()
    mynumber = random.randint (1,3)
    choice=int(input(" "))
    if choice== 1:
        print("you picked rock")
        if mynumber== 1: 
            print("i picked rock as well")
            print("its a tie!")
    Replay = input('Would you like to play again?')
    if Replay == str('y') or str ('yes'):
        menu()


GameOn = True
while (GameOn):
    menu()
    mynumber = random.randint (1,3)
    choice=int(input(" "))
    if choice== 2:
        print("you picked paper")
        if mynumber== 2:
            print("I picked paper as well")
            print("its a tie")

GameOn = True
while (GameOn):
    menu()
    mynumber = random.randint (1,3)
    choice=int(input(" "))
    if choice== 3:
        print("you picked scissors")
        if mynumber== 2:
            print("I picked scissors as well")
            print("its a tie")
    # if '1' in user:
    #         user =int(1)
    #         print("paper"+str(user))
    # elif '2' in user:
    #         user=int(2)
    # elif '3' in user:
    #         user=int(3)
    else:
        print ('pick a different answer')
