import pygame as py
from settings import *

class attack():
    def __init__(self,atkX, atkY, direc):
        super().__init__()
        self.image = py.Surface((20,20))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(topleft = pos)
    


    def attack(self,atkX, atkY, direc):
        if direc  > 0:
            atkX += 30
        if direc  <=0 :
         atkX -= 30
        #py.draw.rect(screen, (5, 250, 50), (atkX, atkY, 20, 20))
        print("attacking at ", atkX," , " ,atkY)
