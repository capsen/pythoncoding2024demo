import pygame
import pgzrun
from pgzhelper import *

class Button(Actor):
    def __init__(self, btnname, pos, callback=None, show=True):
        super().__init__(btnname + '_up', pos)
        self.btnname = btnname
        self.callback = callback
        self.show = show

    def on_mouse_down(self, pos):
        if self.show and self.collidepoint(pos):
            self.image = self.btnname + '_down'

    def on_mouse_up(self, pos):
        if self.show and self.collidepoint(pos):
            self.image = self.btnname + '_up'
            if self.callback:
                self.callback()

    def draw(self):
        if self.show:
            super().draw()