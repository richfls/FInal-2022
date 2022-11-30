import pygame as py
import sys
from mouse import Mouse
from settings import *
from level import Level

#Class-Game-------------------------------------
class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))
        self.clock = py.time.Clock()
        self.level = Level()
        self.start = False
        self.length = 50
    def Start(self):
        while self.start == False:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
            Mouse()
            py.draw.rect(self.screen,(255,255,255),(SCREEN_WIDTH/2-self.length,400,100,50))
            py.draw.rect(self.screen,(255,255,255),(SCREEN_WIDTH/2-self.length,500,100,50))
            py.draw.rect(self.screen,(255,255,255),(SCREEN_WIDTH/2-self.length,600,100,50))
            py.display.update()
    def run(self):
        while True: #GAME-LOOP---------------------------------------
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

            dt = self.clock.tick()/1000 #FPS HANDLER
            self.level.run(dt)
            py.display.update()#WORKS LIKE FLIP BUT CAN UPDAT PORTIONS OF THE SCREEN IF WE WANT
        #END-OF-GAME-LOOP--------------------------------------------------------------------------
if __name__ == '__main__':
    g = Game()
    g.Start()#RUNS THE GAME LOOP
