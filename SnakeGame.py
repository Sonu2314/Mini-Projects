import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.Speed()

#we will declare global constent definitions
Speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE
SEPARATION = 10
SCREEN_HEIGHT = 600
SCREEN_WIDHT = 800
FPS = 25
KEY = {"UP":1, "DOWN":2, "RIGHT":3, "LEFT":4}

#We will initialize screem
screen= pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_HEIGHT),pygame.HWSURFACE)
#We have used HW surface which stands for hardware surface refer to using memory on the video card storing

#draws as opposed to main memory

#resources
score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font..Font(None,48)
Play_again_font = score_numb_font
score_msg = score_font.render("score:",1,pygame.Color("green"))
score_msg_size = score_font.size("score")
background_color = pygame.Color(0,0,0) #we will fill background color as black
black = pygame.Color(0,0,0)

#for clock at the left corner
gameClock = pygame.time.Clock()

def checkColllision(posA.As,posB,Bs):      #As is the size of a and Bs is the size of b
    if(posA.x < posB.x+Bs and posA.x+As > posB.x and posA.y < posB.y+Bs and posA.y+As > posB.y):
        return True
    return False

#to check the boundries here we are not limiting boundries like it can pass through screen and compare

def checkLimits(snake):
    if(snake.x > SCREEN_WIDHT):
        snake.x = SNAKE_SIZE
    if(snake.x<0):        #this will be checked when some part of snake is on other side and on opposite
        snake.x = SCREEN_WIDHT -SNAKE_SIZE
    if(snake.y > SCREEN_HEIGHT):
        snake.y = SNAKE_SIZE
    if(snake.y <0):      #this also same half half
        snake.y = SCREEN_HEIGHT-SNAKE_SIZE

#we will make class for food of the snake lets name it as apple

class Apple:
    def __init__(self,x,y,state):
        self.x =x
        self.y=y
        self.state=state
        self.color=pygame.color.Color("orange")

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,APPLE_SIZE,APPLE_SIZE),0)

class segment:
     #snake move upword
    self.x=x
    self.y=y
    self.direction = KEY["UP"]
    self.color="white"

class snake:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.direction =key["UP"]
        self.stack=[]
        self.stack.append(self)
        blackBox = segment(self.x,self.y+ SEPARATION)
        blackBox.direction=KEY["Up"]
        blackBox.color="NULL"
        self.stack.append(blackBox)

#we will define moves on snake

    def move(self):
        last_element= len(self.stack) - 1
        while(last_element !=0):
            self.stack[last_element].direction = self.stack[last_element].direction
            self.stack[last_element].x = self.stack[last_element - 1].x
            self.stack[last_element].y = self.stack[last_element - 1].y
            last_element -=1
            if(len(self,stack) < 2):
                last_element=self
            else:
                last_segment=self.stack.pop(last_element)
            last_element.direction=self.stack[0].direction
            if(self.stack[0].direction==KEY["UP"]):
                last_segment.y=self.stack[0].y - (SPEED + FPS)
            elif (self.stack[0].direction == KEY["DOWN"]):
                last_segment.y = self.stack[0].y + (SPEED + FPS)
            elif (self.stack[0].direction == KEY["LEFT"]):
                last_segment.x = self.stack[0].x - (SPEED + FPS)
            elif (self.stack[0].direction == KEY["RIGHT"]):
                last_segment.x = self.stack[0].x + (SPEED + FPS)
            self.stack.insert(0,last_segment)

        def getHead(self):      #head of the snake
            return(self.stack[0]) #it will be always 0 index

    #now when snake its food it will grow to for that we will add that food to snake

    def grow(self):
        last_element = len(self.stack) -1





#we will define keys
def getKey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
           if event.key==pygame.K_UP:
               return KEY["UP"]
           elif event.key==pygame.K_DOWN:
               return KEY["DOWN"]
           elif event.key==pygame.K_RIGHT:
               return KEY["RIGHT"]
           elif event.key==pygame.K_LEFT:
               return KEY["LEFT"]
           #for exit
           elif event.key==pygame.K_ESCAPE:
               return KEY["EXIT"]
           #if we want to continue playing again
           elif event.key==pygame.K_Y:
               return "Yes"
           if event.key==pygame.K_N:
               return "No"
           if event.key==pygame.QUIT:
               sys.exit()
def endGame():
    message = game_over_font.render("Game Over",1,pygame.Color("white"))
    message_play_again = play_again_font.render("Play Again ? (Y/N)",1,pygame.Color("green"))
    screen.blit(message,(320,240))
    screen.blit(message_play_again,(320+12,240+40))

    pygame.display.flip()
    pygame.display.update()

    mKey = getKey()
    while(mKey != "exit"):
        if(mKey == "yes"):
            main()
        elif(mKey == "no"):
            break
        mKey = getKey()
        gameClock.tick(FPS)
    sys.exit(0)

def drawScore(score):
    score_numb =score_numb_font.render(str(score),1,pygame.Color("red"))
    screen.blit(score_msg, (SCREEN_WIDHT - score_msg_size[0]-60,10))
    screen.blit(score_numb, (SCREEN_WIDHT - 45,14))

def drawGameTime(gameTime):
    game_time = score_font.render("Time:", 1,pygame.Color("white"))
    game_time_numb = score_numb_font.render(str(gameTime/1000),1,pygame.Color("white"))
    screen.blit(game_time,(30,10))
    screen.blit(game_time_numb,(105,14))

def exitScreen():
    pass

def main():
    score = 0







