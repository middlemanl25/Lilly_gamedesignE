#lilly middleman
#3/23/2022

#main menu for the game creatin functions for menu




import pygame, random
pygame.init()
#variables
WIDTH=700
HEIGHT=700
wb=30
hb=30
#list for messages
Menulists= ['Instructions', 'screen size']
# get colors
colors= {'white':[255,255,255],'red':[255,0,0],'blueish':[102, 153, 255], 'orange':[255, 85, 0], 'purple': [48, 25, 52], 'navy': [5,31,64], 'pink':[200, 3, 75]}

background = colors.get('white')
#sq_color = colors.get('navy')
#making a rand c f the square
colorCheck=True
while colorCheck:
    randColor=random.choice(list(colors))
    if colors.get(randColor)==background:
        randColor=random.choice(list(colors))
    else:
        colorCheck=False
sq_color=colors.get(randColor)
randColor=""
sq_color = colors.get('pink')


#SCREEN
wind=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('circle eats square')

#create different font type
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)

#create titles
text=TITLE_FNT.render('MENU', 1, (255, 0, 0))
wind.fill((255,255,255))
#ger the width of the text
#x value should be = Width/s = wText/s
xt=WIDTH/2-text.get_width()/2
wind.blit(text,(50,50))

#create first button
text=INST_FNT.render('Instructions', 1,(0,255,0))
wind.blit(text,(90,280))

#create square for menu
xs=50
ys=250
square=pygame.Rect(xs,ys,wb,hb)
txty=243
for i in range(7):
    pygame.draw.rect(wind,sq_color, square)
    square.y +-50
pygame.display.update()

pygame.time.delay(100000)
