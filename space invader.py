import pygame
import random
import math

#global Variables
runn = 0
pause = False
pr = False

#Initialize the pygame
pygame.init()

#Create Screen
screen = pygame.display.set_mode((800,600))
background = pygame.image.load('background.png')
pbackground = pygame.image.load('pbackground.png')

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

dull_red = (200,0,0)
dull_green=(0,200,0)

#Score
score_value = 0
font = pygame.font.SysFont(("comicsansms"),32)

textX = 10
textY = 10

#GO text
over_font = pygame.font.SysFont(("comicsansms"),64)

def text_objects(text, font):
    textSurface = font.render(text, True, [0,0,0])
    return textSurface, textSurface.get_rect()

def unpause():
    pause = False

def show_score(x,y):
    score = font.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))

def button(msg,x,y,w,h,ic,ac,action = None):
            global runn
            global  pr
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed() 

            if x+w>mouse[0]>x and y+h>mouse[1]>y :
                pygame.draw.rect(screen, ac, (x,y,w,h))
                if click[0] == 1 and action != None:
                    if action == "play":
                        runn = 1
                    elif action == "quit":
                        pygame.quit()
                        quit()
                    elif action == "continue":
                        pr = True
                        
                        
                    
                #print("heija")
            else:
                pygame.draw.rect(screen, ic, (x,y,w,h))
            smallText = pygame.font.SysFont(("comicsansms"),20)
            textSurf, textRect = text_objects(msg, smallText)
            textRect.center = ((x + (w/2)),(y + (h/2)))
            screen.blit(textSurf,textRect)

def game_intro():
    
    global runn
    intro = True
    
    while intro:
        screen.blit(pbackground, (0,0))
        p = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #screen.fill([255,255,255])
        intro_font = pygame.font.SysFont(("comicsansms"),104)
        TextSurf, TextRect = text_objects("Space Invaders",intro_font)
        TextRect.center = ((400),(300))
        screen.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,dull_green,"play")
        button("Quit!",550,450,100,50,red,dull_red,"quit")
        if runn == 1:
            intro = False
                
        pygame.display.update()

def paused():
    global pr
    global pause
    pause = True
    
    while pause:
        screen.blit(pbackground, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #screen.fill([255,255,255])
        largeText = pygame.font.SysFont(("comicsansms"),114)
        TextSurf, TextRect = text_objects("Paused",largeText)
        TextRect.center = ((400),(300))
        screen.blit(TextSurf, TextRect)

        button("Continue!",150,450,100,50,green,dull_green,"continue")
        button("Quit!",550,450,100,50,red,dull_red,"quit")

        if pr == True:
            pause = False
        
                
        pygame.display.update()
    pr = False
    
    
#Ennemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"  #another possible state is "fire"

def player(x, y):
    screen.blit(playerImg,(x,y))
    
def enemy(x, y, i):
    screen.blit(enemyImg[i],(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16,y + 10))
    
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((bulletX - enemyX)**2 + (bulletY - enemyY)**2)
    if distance < 27:
        return True
    else:
        return False

game_intro()

#Game Loop
running = True
while running:
    
    
    screen.fill((124,124,1))    
    
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 5.4
            if event.key == pygame.K_p:
                pause = True
                paused()
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                
    
    playerX += playerX_change     
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
     
        #Enemy Movement
    for i in range(num_of_enemies):
        
        #GAme Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        
        enemyX[i] += enemyX_change[i]      
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        #collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value+=1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i], i)
        
    #Bullet Movement
    if bulletY <= 0 :
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        
    
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()


pygame.quit()
quit()
    
