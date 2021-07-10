import pygame
from pygame.locals import *
pygame.init()

#class for flappybird sprite
class Bird(pygame.sprite.Sprite):

  #loads the image and sets the position of the sprite rectangle
  def __init__(self):
    super().__init__()
    self.y_value = 150
    self.image = pygame.image.load("bird.png")
    self.rect = pygame.Rect(50, self.y_value, 50, 50)

  #updates the y-position of the bird and redraws the rectangle at that location
  def updateposition(self, ypos):
    self.rect.y = self.rect.y - ypos
