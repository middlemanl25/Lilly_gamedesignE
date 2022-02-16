#lilly middleman
#2/8/22
#word game with 3 levels:

#       1. Fruits
#       2. Animals
#       3. Comuputor Parts
# Choice:

# Create word list
from modulefinder import IMPORT_NAME

import os, random
os.system('cls')

def menu():
    print('##################################################')
    print('#             Guess A word Menu                   #')
    print('#                                                 #')
    print('#              1. Fruits                          #')
    print('#              2. Animals                         #') 
    print('#              3. Computor parts                  #')
    print('#                   select your choice            #')
    print('##################################################')
choice= 0
word = ""
guess= ""
def selectWord():
    global word
    
    fruits= ["banana", "grape","watermelon", "papaya", "orange", "tomato",
    "mango", "kiwi", "strawberry","blackberry", "apple"]
    Animals= ["dog", "cat","monkey", "tiger", "snake", "shark",
    "lizard", "kangaroo", "whale","fish", "duck"]
    computorparts= ["mouse", "keyboard", "screen", "trackpad", "battery"]
    # size=(len(fruits))
    # randy= random.randint(0,size)
    # print(randy)
    # word=fruits[randy]
    # print(word)
    choice=int(input("what is your choice? "))
    if choice==1:
        word=random.choice(fruits)
    elif choice==2:
        word=random.choice(Animals)
    else:
        word=random.choice(computorparts)



def guessFunction():
    global guess
    check=True
    while check:
        try:
            guess=input("\nenter a letter to guess the word")
            if guess.isalpha() and len(guess)==1:
                check=False
            else:   
                print ('enter a letter to start playing')
        except ValueError:
            print("keep guessing")
menu()
gameOn=True
tries=0
letterGuessed=""
selectWord()
while gameOn:
    guessFunction()
    letterGuessed += guess #letterGuessed=letterGuessed+guess
    if guess not in word:
        tries +=1
        print(tries)# for testing delete after when game is ready
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter +=1
        else:
            print("_", end=" ")
    if tries >6:
        print("\n sorry run out chances ")
        #playGame( ask if they want to play again)
    if countLetter == len(word):
        print ("\n you guessed!")
        menu()

def selectWord(animals):
    global word
    os.system('cls')
    Animals= ["dog", "cat","monkey", "tiger", "snake", "shark",
    "lizard", "kangaroo", "whale","fish", "duck"]

def guessFunction(animals):
    global guess
    check=True
    while check:
        try:
            guess=input("\nenter a letter to guess the word ")
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                print ('Only one letter please')
        except ValueError:
            print("only one letter please")

gameOn=True
tries=0
letterGuessed=""
selectWord()
while gameOn:
    guessFunction()
    letterGuessed += guess #letterGuessed=letterGuessed+guess
    if guess not in word:
        tries +=1
        print(tries)# for testing delete after when game is ready
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter +=1
        else:
            print("_", end=" ")
    if tries >6:
        print("\n sorry run out chances ")
        #playGame( ask if they want to play again)
    if countLetter == len(word):
        print ("\n you guessed!")
        menu()




