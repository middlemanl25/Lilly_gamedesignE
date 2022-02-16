# Lilly Middleman
# lists and list methods
import os, random
os.system("cls")
fruits= ["banana", "grape","watermelon", "papaya", "orange", "tomato",
    "mango", "kiwi", "strawberry","blackberry", "apple"]
#length of your array
size= len(fruits)
print(size)
fruits.append("rambutan")
for i in range(size+1): #13 is not included
    print(fruits[i])
print(fruits[size-1])
print(fruits[-2])
print(fruits.count('banana'))
list2=[3,6,8,9,10]
fruits.append(list2)
print("append\n",fruits)
fruits.extend(list2)
print("extend \n",fruits)
fruits.insert(2,"dragon fruit")
print(fruits)