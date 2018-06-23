# SNAKE GAME

import pygame
import sys
import random
import time

# check for initializing errros
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, Exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame succcessfully initialized!")

# Play surface
playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake Game")

# Colors
red = pygame.Color(255,0,0)        #Game over #Color(r,g,b)
green = pygame.Color(0,255,0)      #Food
black = pygame.Color(0,0,0)        #Score
white = pygame.Color(255,255,255)  #Background
brown = pygame.Color(165,42,42)    #Snake
purple = pygame.Color(75,0,130)   #background 2
# FPS Controller : Frames per second
fpsController = pygame.time.Clock()

# Important variables
snakePos = [100,150]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0
# score function
def showScore(choice = 1):
    scoreFont = pygame.font.SysFont('monaco', 30)
    Ssurface = scoreFont.render("Score : {0}".format(score), True, black)
    Srect = Ssurface.get_rect()
    if choice == 1:                  # while game is running, score at top left
        Srect.midtop = (50, 10)
    else:
        Srect.midtop = (360, 120)    #when game over score at centre
    playSurface.blit(Ssurface, Srect)



# Game Over function
def gameOver():
    myFont = pygame.font.SysFont('monaco',72)
    GOsurface = myFont.render("GAME OVER!",True,red)
    GOrect = GOsurface.get_rect()
    GOrect.midtop = (360,20)
    playSurface.blit(GOsurface,GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()    # pygame exit
    sys.exit()       # console exit

# Logic of game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):    #ord gives ascii value
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))   #create an event

    # Vallidation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # UPDATE SNAKE POSITION
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # SNAKE BODY MECHANISM
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
    foodSpawn = True

    #Color of background surface
    playSurface.fill(purple)


    for pos in snakeBody:
        pygame.draw.rect(playSurface, brown,pygame.Rect(pos[0],pos[1],10,10) )

    pygame.draw.rect(playSurface, green, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    #Gameover conditon
    if snakePos[0] > 710 or snakePos[0] < 0:  # hitting x boundary
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:  # hitting y boundary
        gameOver()

    for block in snakeBody[1:]:              # hitting itself
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip()
    fpsController.tick(18)
