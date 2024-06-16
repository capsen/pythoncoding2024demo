import pgzrun
from pgzhelper import *
from sprite import Sprite
from button import Button

WIDTH = 800
HEIGHT = 600
step = 0


sprites = []
buttons = []

background = Actor("baseball")
#Add your code below
abby = Sprite("abby-a")
abby.scale = 0.5
sprites.append(abby)

devin = Sprite("devin-a")
devin.scale = 0.5
sprites.append(devin)

def next():
    global step
    step += 1
    step_changed()

next_button = Button("next", (700, 400), next)
buttons.append(next_button)

def step_changed():
    print(step)
    if step == 0:
        abby.show = False
        devin.show = False
    elif step == 1:
        abby.show = True
        devin.show = True
        abby.message="Hi, how are you?"


def draw():
    screen.clear()
    background.draw()
    for s in sprites:
        s.draw()
    for b in buttons:
        b.draw()
    # elements need to be draw here

def update():
    # any global variable need to be updated need specify global
    pass

def on_mouse_down(pos):
    for b in buttons:
        b.on_mouse_down(pos)

def on_mouse_up(pos):
    for b in buttons:
        b.on_mouse_up(pos)

step_changed()

pgzrun.go() # Must be last line