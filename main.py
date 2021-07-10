#Global Variables

#Setting up the display
import pygame, sys
from pygame.locals import *
pygame.init()
import random
from bird import Bird
from pipes import Pipes
flappybird = Bird()
greenpipes = Pipes()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Flappy Bird!")
background = pygame.image.load("background.png")
score = 0
white = (255,255,255)
screen_type = "start"

#Game Fonts and Text
small_font = pygame.font.Font('freesansbold.ttf', 25)
big_font = pygame.font.Font('freesansbold.ttf', 50)
score_text = small_font.render("Score: " + str(score), True, white)

#Function that has code for the "start" screen
def start():
  global screen_type

  while screen_type == "start":

    screen.blit(background, (0,0))

    #Title text
    beginning_text = big_font.render("Flappy Bird", True, white)
    screen.blit(beginning_text, (110, 50))

    #Play button
    play_button_rect = pygame.Rect(210, 150, 100, 50)
    play_button = pygame.draw.rect(screen, (0,0,255), play_button_rect)
    play_button_text = small_font.render("Play", True, white)
    screen.blit(play_button_text, (230,160))

    #How to Play button
    instruct_button_rect = pygame.Rect(170, 290, 200, 50)
    instruct_button = pygame.draw.rect(screen, (0,0,255), instruct_button_rect)
    instruct_button_text = small_font.render("How to play", True, white)
    screen.blit(instruct_button_text, (190,300))

    #Quit button
    quit_button_rect = pygame.Rect(210, 400, 100, 50)
    quit_button = pygame.draw.rect(screen, (0,0,255), quit_button_rect)
    quit_button_text = small_font.render("Quit", True, white)
    screen.blit(quit_button_text, (230,410))

    #When the Play button is pressed, the screen changes to the game screen. When the Instruction button is pressed, the screen changes to the instruction screen.
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()

      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if play_button.collidepoint(mouse):
          screen_type = "game"
        if instruct_button.collidepoint(mouse):
          screen_type = "instruction"
        if quit_button.collidepoint(mouse):
          sys.exit()

    pygame.display.update() 

#Function that has code for the "instructions" screen
def instructions():
  global screen_type

  while screen_type == "instruction":

    screen.blit(background, (0,0))

    #Title and Instructions text
    Instruct = big_font.render("How to play", True, white)
    Instructions1 = small_font.render("-Press the spacebar to fly.", True, white)
    Instructions2 = small_font.render("-Do not touch the poles.", True, white)
    Instructions3 = small_font.render("-Do not fly too high or touch the ground.", True, white)
    screen.blit(Instruct, (120, 80))
    screen.blit(Instructions1, (20, 170))
    screen.blit(Instructions2, (20, 220))
    screen.blit(Instructions3, (20, 270))

    #Back button
    back_button_rect = pygame.Rect(200, 320, 100, 50)
    back_button = pygame.draw.rect(screen, (0,0,255), back_button_rect)
    back = small_font.render("Back", True, white)
    screen.blit(back, (220, 330))

    #When the back button is pressed, the screen changes to the start screen
    for event in pygame.event.get():
      if event.type == QUIT:
          sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if back_button.collidepoint(mouse):
          screen_type = "start"

    pygame.display.update() 

#Function that has code for the "game" screen
def game():
  global screen_type
  global score
  global score_text

  FPS = 30
  fpsClock = pygame.time.Clock()

  while screen_type == "game":

    #Makes pipes continuously move backwards
    greenpipes.updateposition(10)
    
    #Moves bird continuously go down
    flappybird.updateposition(-5)
        
    #If the pipe's x value touches the -40 x value, then it resets at the 500 x-value and also randomizes the pipes y value
    if greenpipes.x_value == -40:
      greenpipes.x_value = 500
      greenpipes.y_value = random.randint(-260,-25)

    #If the bird touches the ground or goes too high the game ends
    if flappybird.rect.y ==  420 or flappybird.rect.y == -100:
      screen_type = "end"

    #When the bird passes through the pipes, 1 point is added to the score
    if greenpipes.x_value < 50 and greenpipes.x_value > 30:
      score += 1
      score_text = small_font.render("Score: " + str(score), True, white )

    #draws the background and scoreboard
    screen.blit(background, (0,0))
    screen.blit(score_text, (200, 50))

    #draws both of the pipes
    pygame.draw.rect(screen, (0, 200, 0), greenpipes.rectangle1)

    pygame.draw.rect(screen, (0, 200, 0), greenpipes.rectangle2)

    #draws the flappybird
    screen.blit(flappybird.image, flappybird.rect)

    #if the bird and the upper or lower rectangle collide, the game ends
    if (greenpipes.x_value == 50 and greenpipes.rectangle1.colliderect(flappybird.rect)) or (greenpipes.x_value == 50 and greenpipes.rectangle2.colliderect(flappybird.rect)):
      screen_type = "end"

    #when spacebar is pressed, the flappybird goes up 75 pixels
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          flappybird.updateposition(75)

    pygame.display.update()
    fpsClock.tick(FPS)

#Function that resets all the variables when a new game is started
def reset():
  global score_text
  global score

  flappybird.rect.y = 150
  greenpipes.x_value = 500
  greenpipes.y_value = 0
  greenpipes.height = 300
  score = 0
  score_text = small_font.render("Score: " + str(score), True, white )

#Function that has code for the "end" screen
def end():
  global screen_type
  global score
  global score_text

  while screen_type == "end":

    screen.blit(background, (0,0))
    game_over_text = big_font.render("Game Over ", True, white)
    screen.blit(game_over_text, (115, 50))
    final_score_text = small_font.render("Final Score: " + str(score), True, white)
    screen.blit(final_score_text, (170, 120))

    playagain_button_rect = pygame.Rect(180, 220, 150, 50)
    playagain_button = pygame.draw.rect(screen, (0,0,255), playagain_button_rect)
    playagain_text = small_font.render("Play again ", True, white )
    screen.blit(playagain_text, (190, 230))

    mainmenu_button_rect = pygame.Rect(180, 310, 150, 50)
    mainmenu_button = pygame.draw.rect(screen, (0,0,255), mainmenu_button_rect)
    mainmenu_text = small_font.render("Main menu ", True, white )
    screen.blit(mainmenu_text, (190, 320))

    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if playagain_button.collidepoint(mouse):
          reset()
          screen_type = "game"
        if mainmenu_button.collidepoint(mouse):
          reset()
          screen_type = "start"
          
         
    pygame.display.update() 

#Main function that runs the entire game
def main():
  global screen_type

  while True:
    if screen_type == "start":
      start()
    if screen_type == "instruction":
      instructions()
    if screen_type == "game": 
      game()
    if screen_type == "end":
      end()

#calls the main function
main()
