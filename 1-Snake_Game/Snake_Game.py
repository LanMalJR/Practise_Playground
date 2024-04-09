#!/usr/bin/env python3
import tkinter
import random  

ROWS = 25
COLMS = 25
TITLE_SIZE = 25

WINDOW_WIDTH = TITLE_SIZE * COLMS
WINDOW_HEIGHT = TITLE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y= y

#Game Window
Window = tkinter.Tk()
Window.title("Snake")
Window.resizable(False, False)

Canvas = tkinter.Canvas(Window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
Canvas.pack()
Window.update()

#Center the window
WINDOW_WIDTH = Window.winfo_width()
WINDOW_HEIGHT = Window.winfo_height()
SCREEN_WIDTH = Window.winfo_screenmmwidth
SCREEN_HEIGHT = Window.winfo_screenmmheight

Window_X = int((SCREEN_WIDTH/2) - (WINDOW_WIDTH/2))
Window_Y = int((SCREEN_HEIGHT/2) - (WINDOW_HEIGHT/2))

#f_string
#format "(w)x(h)+(x)+(y)"
Window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+({Window_X}+{Window_Y})")

#Initialize game
Snake = Tile(5*TITLE_SIZE, 5*TITLE_SIZE) #Single title, is a snakes head
#Food = 

def Draw():
    global Snake

    #Draw snake
    Canvas.create_rectangle(Snake.x, Snake.y, Snake.x + TITLE_SIZE, Snake.y + TITLE_SIZE, fill = "yellow")

    Window.after(100, Draw) #100ms = 1/10 second -> 10 frames/sec

Window.mainloop
