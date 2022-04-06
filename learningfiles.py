#lilly middleman
#learningfiles
#a.open/create a file
#b. write 'w'
#c. append 'a'
#d. read 'r'
#e. close()

import pygame,os, datetime
os.system('cls')
date=datetime.datetime.now()
score=123
name='Jesse'
print(date.strftime('%m,%d,%Y'))
scoreLine=str(score)+" "+name+" "+date.strftime('%m,%d,%Y')
print(scoreLine)
#open a file and write in it 
myFile=open('sce.txt', 'w')
myFile.write(scoreLine)

myFile.close()
score=345
name='Jay'
print(date.strftime('%m,%d,%Y'))
scoreLine=str(score)+" "+name+" "+date.strftime('%m,%d,%Y')
myFile=open('sce.txt', 'a')
myFile.write(scoreLine)
myFile.close()
myFile=open('sce.txt', 'r')
lines=myFile.readlines()
print(lines)
myFile.close()
lines=myFile.readlines()
print(lines)
myFile.close()