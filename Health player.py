import pygame as py
from settings import *
from timer import *

class Player(py.sprite.Sprite): #Child class of pygames sprite class
    def __init__(self, pos, group):
        super().__init__(group)#this gives this class access to the functions inside the group class
        self.run = False

        #health bar------------- (change what you need - simon)
        self.image = py.Surface((40, 40))
        self.image.fill(((240, 240, 240)))
        self.rect = self.image.get_rect(center = (400, 400))
        self.current_health = 200
        self.target_health = 500
        self.maximum_health = 1000
        self.health_bar_length = 400
        self.health_ratio = self.maximum_health / self.health_bar_length
        self.health_change_speed = 5
        #end of health bar------------------
        #general setup----------
        self.rect = self.image.get_rect(center = pos)
        #movement---------
        self.direction = py.math.Vector2()#Velocity
        self.pos = py.math.Vector2(self.rect.center)#player position
        self.speed = 200

    def input(self): #Keyboard movements
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

#health bar function------------------------------
    #def advanced_health(self):
       # transition_width = 0
        #transition_color = (255, 0, 0)

        #if self.current_health < self.targer_health:
        #    self.current_health += self.health_change_speed
        #    transition_width = int((self.target_health - self.current_health)/self.health_ratio)
        #    transition_color = (0, 255, 0)
        #if self.current_health > self.targer_health:
         #   self.current_health -= self.health_change_speed
         #   transition_width = int((self.target_health - self.current_health)/self.health_ratio)
         #   transition_color = (255, 255, 0)

        #health_bar_rect = py.Rect(10, 45, self.current_health / self.health_ratio, 25)
        #transition_bar_rect = py.Rect(health_bar_rect.right, 45, width, 25)

        #py.draw.rect(screen, (255, 0, 0), health_bar_rect)
        #py.draw.rect(screen, transition_color, transition_bar_rect)
        #py.draw.rect(screen, (255, 255, 255), (10, 45, self.health_bar_length,25), 4)


#end of health bar function -------------------------------
    def update(self, dt):
        self.input()
        self.move(dt)
        #self.advanced_health()
