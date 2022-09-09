import pygame as pg
import numpy as np
from controls_colliding import ai_movement, obj_user_movement

pg.init()

#screen specs
background = (0,0,0)
FPS = 60
size = width, height = 900, 600
number_of_rects = 5
rects = []
run = True
COLOR = (0,255,0)

screen = pg.display.set_mode(size)
clock = pg.time.Clock()


Font = pg.font.SysFont(None, 24) #none tells us that we dont specify the "font" style
#it's going to be a defaoult systems font. Secound part is the fontsize

def draw_text(screen, text: str, position: tuple) -> None:
    img = Font.render(text, True, (0,255,255))
    screen.blit(img, position)

def random_pionts_2d(n):
    vector_x = np.random.randint(901, size=n)
    vector_y = np.random.randint(601, size=n)
    return vector_x, vector_y

def random_rects(n):
    rects = []
    x_arr, y_arr = random_pionts_2d(n)
    for i in range(len(x_arr)):
        x, y = x_arr[i], y_arr[i]
        r = pg.Rect(x, y, 25, 25)
        rects.append(r)
    
    return rects

def random_squares(n):
    rects = []
    x_arr, y_arr = random_pionts_2d(n)
    for i in range(n):
        x, y = x_arr[i], y_arr[i]
        square = Rect_Object(x, y, 25, 25)
        rects.append(square)

    return rects
#objects
Obj_main1 = pg.Rect(95,95,215,215)
obj_main2 = pg.Rect(100,100,200,200)

class Rect_Object: #do poprawy !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.top = pg.Rect(x, y, width, 1)
        self.left = pg.Rect(x, y, 1, height)
        self.bottom = pg.Rect(x, y+height, width, 1)
        self.right = pg.Rect(x+width, y, 1, height)
        self.width = width
        self.height = height

    def move(self, keys_pressed) -> None:
        obj_user_movement(keys_pressed, self.top, top=self.height)
        obj_user_movement(keys_pressed, self.left, left=self.width)
        obj_user_movement(keys_pressed, self.bottom, bottom=self.height)
        obj_user_movement(keys_pressed, self.right, right=self.width)

    def move_bot(self, id: int, velocity: int) -> None:
        ai_movement(self.top, id, velocity, bottom=self.height, right=self.width)
        ai_movement(self.left, id, velocity, right=self.width, bottom=self.height)
        ai_movement(self.bottom, id, velocity, top=self.height, right=self.width)
        ai_movement(self.right, id, velocity, left=self.width, bottom=self.height)
        self.normalize_move_bot()  #if you're curuis whats its doing
                                    #just commentout this method, and y'll see ;)
    def normalize_move_bot(self) -> None:
        self.left.x, self.left.y = self.top.x, self.top.y
        self.bottom.x, self.bottom.y = self.top.x, self.top.y + self.height
        self.right.x, self.right.y = self.top.x + self.width, self.top.y

    def draw(self, Screen)  -> None:
        pg.draw.rect(Screen,(255,255,255),self.top,1)
        pg.draw.rect(Screen,(255,255,255),self.left,1)
        pg.draw.rect(Screen,(255,255,255),self.bottom,1)
        pg.draw.rect(Screen,(255,255,255),self.right,1)


obj_main3 = Rect_Object(500, 150, 20, 100)

        
        


