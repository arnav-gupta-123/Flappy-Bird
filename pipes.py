import pygame
from pygame.locals import *
pygame.init()

#class for the pipe sprites
class Pipes(pygame.sprite.Sprite):

  #sets the pipe position and rectangles
  def __init__(self):
    super().__init__()
    self.x_value = 500
    self.y_value = 0
    self.height = 300 
    self.rectangle1 = pygame.Rect(self.x_value, self.y_value, 30, self.height)
    self.rectangle2 = pygame.Rect(self.x_value, self.y_value + self.height + 150, 30, self.height) 

  #changes the pipes x-position and redraws the rectangles at that location
  def updateposition(self, xpos):
    self.x_value = self.x_value - xpos
    self.rectangle1 = pygame.Rect(self.x_value, self.y_value, 30, self.height)
    self.rectangle2 = pygame.Rect(self.x_value, self.y_value + self.height + 150, 30, self.height) 
