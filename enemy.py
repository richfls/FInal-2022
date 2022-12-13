import pygame 
import random
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((64,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)
        self.isOnGround = False
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
    def gravity(self):
        #Gravity function 
        self.direction.y += .8
        self.rect.y += self.direction.y 

    def input(self):
        self.atk = Attack(self.rect.x,self.rect.y,self.direction.x)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
                self.atk.attack()
        if keys[pygame.K_SPACE] == True:
            self.jump()
            self.isOnGround = False
        elif keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
                
    def jump(self):
        self.direction.y = -16
