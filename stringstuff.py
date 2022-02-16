#lilly middleman
#2/2/22
#Strings are arrays of characters
#Has Many Functions

import os, random
os.system ('cls')
myName = "lilly middleman"
myStatement = """guess a letter

guess a letter"""
#^^^ IF I USE TRIPLE QUOTATION MARKS - IT PRINTS EXACTLY HOW I TYPE (WITH THE SPACES AND EVERYTHING)
print (myName[6])
#^^ It takes the 6th letter and prints it
print (myStatement)
if 'yay' in myStatement:
    print ('true')
#Checks if the word is there then will give a output
print ('expert' not in myStatement)
#not in or in will make it check the statemtn and will print true or false depending on ur code
INDEX= myName.find("a")
print(INDEX)
#finding the length of your word
wordLen= len(myName)
print(wordLen) #your last index is len-1
#for loop in range 0 to limit
for i in range(wordLen-1):
    if "a" in myName[i]:
        print(i, end=", ")
print("")
print("done")
myStatement= myStatement.upper()
print(myStatement)
letter=input("dear user, please give us a nice letter")
print("thank you the letter is "+ letter)
if letter in myStatement:
    print ("GREAT")

check=True
while check:
    letter=input("dear user, please give us a nice letter")
    if len(letter)>1 or not letter.isalpha():
        print("bad")
    else:
        check=False
print("ready to play the game")
for elem in myStatement:\
    print(elem, end=" ")
guess=random.choice(myName)
print(guess)
words= ["Radio", "Clues", "Suite", "Peter", "Robot"]
word=random.choice(words)
print(word)    
for i in range(len(word)):
    if letter == word[i]:
        print(letter, end=" ")
        print("_", end=" ")