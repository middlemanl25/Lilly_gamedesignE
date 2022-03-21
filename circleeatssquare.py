#Lilly Middleman
#learning how to draw circles and squares
#use keys to move objects 
#using dictionary 

#objectiven of the game is for the rectangle to run away from the circle, if they collide the cirlce eats the square
#the circle will get larger and a new rectangle should apear somewhere on the screen

import os, random, time, pygame
from shutil import move
from turtle import width 
#initalze pygame
pygame.init()

#declare constants, variables, list, dictionaries, any object

WIDTH=700
HEIGHT=700
check=True

#square variables
xs=20
ys=20
wbox=30
hbox=30
#circle variables
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, WIDTH-rad)
#creating the rec object
square=pygame.Rect(xs,ys,wbox,hbox)

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('circle eats square')
#define colors
colors={'white':[255,255,255], 'red':[2555,0,0], 'aqua':[102,153,255],
 'orange':[255,85,0], 'purple':[48,25,52],'navy':[5,31,64], 'pink':[200,3,75]}

#get colors
backgrounds= colors.get('pink')
sq_color=colors.get('navy')
cr_color=colors.get('white')
while check:
     screen.fill(backgrounds)
     for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
            square.x=move
    
     
     keys=pygame.key.get_pressed() 
     if keys [pygame.K_a]:
        square.x=move 
     if keys: 
pygame.draw.rect(screen, sq_color, square)
pygame.draw.circle(screen, cr_color,  (xc,yc), rad)

pygame.display.update()
pygame.time.delay(1000) 