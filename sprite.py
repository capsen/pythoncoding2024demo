import pygame
import pgzero
from pgzhelper import *

mod = sys.modules['__main__']

class Sprite(Actor):
    def __init__(self, image, pos=POS_TOPLEFT, anchor=ANCHOR_CENTER, **kwargs):
        self.show=True
        self.message=""
        self.show = True
        super().__init__(image, pos, anchor, **kwargs)

    def draw(self):
        if self.show:
            super().draw()
            if(self.message):
                self.draw_speak()

    def draw_speak(self):
        position = self.topleft
        messagebox_width = 100
        messagebox_height = 70
        messagebox_x = position[0] + 5 + self.width
        messagebox_y = position[1] - 5 - messagebox_height
        left_radius = 0
        right_radius = 10
        
        if( messagebox_x + messagebox_width > mod.screen.surface.get_width()):
            messagebox_x = position[0] - 5 - messagebox_width
            left_radius=10
            right_radius=0
        
        if(position[1] - messagebox_height - 5 < 0):
          messagebox_y = 0 + 5 + messagebox_height
            
        pygame.draw.rect(mod.screen.surface, (48, 141, 70), pygame.Rect(messagebox_x, messagebox_y, messagebox_width, messagebox_height),  0, 0, 10, 10, left_radius, right_radius)
        pygame.draw.rect(mod.screen.surface, (255,0,0), pygame.Rect(messagebox_x, messagebox_y, messagebox_width, messagebox_height),  4, 0, 10, 10, left_radius, right_radius)
        mod.screen.draw.textbox(self.message, (messagebox_x + 5, messagebox_y+5, messagebox_width-10, messagebox_height-10) )