import pygame as py
from settings import *

class Attack():
    def __init__(self,a,b,c):
        super().__init__()
        self.atkx = a
        self.atky = b
        self.direc = a


    def attack(self):
        if self.direc  > 0:
            self.atkx += 30
        if self.direc  <=0 :
            self.atkx -= 30
        print("attacking at ",self.atkx," , " ,self.atky )
        py.draw.rect(screen,(0,255,255),(self.atkx,self.atky,32,64))
        py.display.flip()
