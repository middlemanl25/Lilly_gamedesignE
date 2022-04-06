#lillymiddleman
#learning how to draw circles and rectangles

#use keys to move objects

#Using Dictionaries

 

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square,

#circle will  get larger, and a new rect should appear somewhere on the screen

# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               jump

#initialize pygame

import os, random, time, pygame, math
from re import S
os.system('cls')
from turtle import back
from pickle import TRUE
#initialize pygame

pygame.init()

 

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('LEVEL II')
bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')
character=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')
screen.blit(bg,(0,0))
screen.blit(chart,(200,200))
pygame.display.update()
pygame.time.delay(3000)

move=S
check=True