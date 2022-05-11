#lilly middleman
#Practice with pygame
import os, time, random,math
import pygame, turtle
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE
#initialize pygame
pygame.init()
#variables, constants, and objects
import os, random, time, pygame, math, datetime
os.system('cls')
name=input("What is your name? ")
#initialize pygame
pygame.init()

#scree size
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30
MAIN=True
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False
SCORE=False
SC_SIZE=False
BG_COLOR=False
SPRITE=False
ON_OFF=False
sc=True
#menu layout
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size','Backgrnd Color','Icon','']
SC_Sizelist=['1000 x 1000', '2000 x 2000', '3000 x 3000']
check=True
 #for the while loop

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle eats Square')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')
BLACK=(0,0,0)
#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((255,255,255))
    
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))

def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10)
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
def instr():
    print("in instr")
    myFile=open('ClassStuff\CircleEatsSquare\instructions.txt', 'r')
    yi=150
    stuff= myFile.readlines()

    print(stuff)
    for line in stuff:
        print(line)
        text=INST_FNT.render(line, 1, BLACK)
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+=50
    myFile.close()
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    # when y write it erases the prev 
    myFile=open('ClassStuff\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def scoreBoard():
    myFile=open('sce.txt', 'r')
    yi=150
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    j=0
    for i in range(N, -1, -1):
        print(i,stuff[i])
        
        temp[j]=stuff[i]
        j +=1
    for t in range(5):
        text=INST_FNT.render(stuff[i], 1, BLACK)
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+=50
    
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine='\n'+str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
    global HEIGHT, WIDTH, screen
 
    # when y write it erases the prev 
    myFile=open('ClassStuff\CircleEatsSquare\sce.txt','a') 
    myFile.write(scoreLine)
    myFile.close()

def playGame():
        
    import pygame
import time
import random
pygame.init()
banana=pygame.image.load("images\Pygame-Tutorials-master\Game\\banana.png")
grape=pygame.image.load("images\Pygame-Tutorials-master\Game\grape.png")
strawberry=pygame.image.load("images\Pygame-Tutorials-master\Game\strawberry.png")

banana=pygame.transform.scale(banana,(60,64))
grape=pygame.transform.scale(grape,(64,64))
strawberry=pygame.transform.scale(strawberry,(64,64))

randomfruits = [(banana), (grape),(strawberry)]

HEIGHT=False
WIDTH=False
CRadius=15
move=5
fruit=random.choice(randomfruits)
print(fruit)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
dis_width = 800
dis_height  = 600
xc=random.randint(0,dis_width)
yc=random.randint(0,dis_height)
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Lilly')


 
game_over = False
 
x1 = dis_width/2
y1 = dis_height/2
 
snake_block=10
 
x1_change = 0
y1_change = 0
 
clock = pygame.time.Clock()
snake_speed=30
 
font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
 
    # if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
    if x1 >= dis_width or y1 >= dis_height or y1 < 0 or x1<0:
        game_over = True
 
    x1 += x1_change
    y1 += y1_change
    dis.fill((0,0,255))
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    dis.blit(fruit,(xc,yc))
    
    pygame.display.update()
 
    clock.tick(snake_speed)
 
message("You lost",red)
pygame.display.update()
time.sleep(2)
 
pygame.quit()
quit() 
#sq_color=colors.get('navy')
#Making a rand c f the square
changeColor()
#Beginning of main program
sq_color=colors.get(randColor)
keys=pygame.key.get_pressed()
mouse_pos=(0,0)
screCk=True
first=True
# add xm and ym
while check:
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            #xm= mouse_pos[0]
            #ym=
        # print(mouse_pos)
    keys=pygame.key.get_pressed() #this returns a list
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST and first:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        first=False
    if INST:
        if keys[pygame.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True
    if SETT:
        screen.fill(background)
        TitleMenu("SETTINGS")
        MainMenu(SettingList)
        if keys[pygame.K_ESCAPE]:
            SETT=False
            MAIN=True
    if LEV_I:
        screen.fill(background)
        playGame()
        print("I shld be t")
        LEV_I=False
        MAIN=True
        mouse_pos=(0,0)
    if LEV_II:
        screen.fill(background)
        TitleMenu("LEVEL II")
        if keys[pygame.K_ESCAPE]:
            LEV_II=False
            MAIN=True
    if LEV_III:
        screen.fill(background)
        TitleMenu("LEVEL III")
        if keys[pygame.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    if SCORE and screCk:
        screen.fill(background)
        TitleMenu("SCOREBOARD")
        scoreBoard()
        #call funct t print scres
        screCk=False
    if SCORE:
        if keys[pygame.K_ESCAPE]:
            SCORE=False
            MAIN=True
            screCk=True
    if SC_SIZE:
        screen.fill(background)
        TitleMenu('screensize')
        MainMenu(SC_Sizelist)
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))and MAIN :
        MAIN=False
        INST=True
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))and MAIN :
        MAIN=False
        SETT=True  
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))and MAIN :
        MAIN=False
        LEV_I=True   
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))and MAIN :
        MAIN=False
        LEV_II=True   
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480))or LEV_III :
        MAIN=False
        LEV_III=True   
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530))or SCORE :
        MAIN=False
        SCORE=True 
    if SETT and sc:
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))and SETT :
            SETT=False
            SC_SIZE=False
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))and SETT :
            SETT=False
            BG_COLOR=True  
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))and SETT :
            SETT=False
            SPRITE=True   
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))and SETT :
            SETT=False
            ON_OFF=True      
        if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >550 and mouse_pos[1] <580)) :
            screen.fill(background)
            
        keepScore(121)
        text=INST_FNT.render("dont forget to update the score", 1, BLACK)
        screen.blit(text, (40,200))
        text=INST_FNT.render("before you leave", 1, BLACK)
        screen.blit(text, (40,300))
        text=INST_FNT.render("Thanks for playing", 1, BLACK)
        screen.blit(text, (40,400))
        pygame.display.update()
        pygame.time.delay(50)
        MAIN=False
        SCORE=False 
        pygame.time.delay(3000)
        check=False
    pygame.display.update()
    pygame.time.delay(10)

os.system('cls')
pygame.quit()