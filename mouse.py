import pygame as py
from settings import *

class Mouse:
    def __init__(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.MOUSEBUTTONDOWN:
                if py.MOUSEBUTTONDOWN:
                    print("click")
