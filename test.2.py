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