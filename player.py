import pygame as py
from settings import *
from timer import *

class Player(py.sprite.Sprite): #Child class of pygames sprite class
    def __init__(self, pos, group):
        super().__init__(group)#this gives this class access to the functions inside the group class
        self.run = False

        self.image = py.Surface((32,64))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)#set the pos to be in the center of the rect
        #general setup
        self.rect = self.image.get_rect(center = pos)
        #movement
        self.direction = py.math.Vector2()
        self.pos = py.math.Vector2(self.rect.center)
        self.speed = 200
        

    def input(self):
        keys = py.key.get_pressed()
        if keys[py.K_LSHIFT]:
            self.run = True
            if keys[py.K_UP]:
                self.direction.y = -2
                self.status = "up"
            elif keys[py.K_DOWN]:
                self.direction.y = 2
                self.status = "down"
            elif keys[py.K_RIGHT]:
                self.direction.x = 2
                self.status = "right"
            elif keys[py.K_LEFT]:
                self.direction.x = -2
                self.status = "left"
            else:
                self.direction.y = 0
                self.direction.x = 0

        elif keys[py.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[py.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        elif keys[py.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[py.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.y = 0
            self.direction.x = 0
            self.run = False

       
        print(self.direction)

    def move(self, dt):
        #print(self.direction)
        #horizontal movement
        if self.run == True and self.direction.magnitude() > 0 :
           self.direction = self.direction
        elif self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y 

    def update(self, dt):
        self.input()
        self.move(dt)

