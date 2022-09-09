from xmlrpc.client import Boolean
import pygame as pg
import numpy as np

background = (0,0,0)
size = width, height = 900, 600
VEL = [10,10]

pg.init()

#for obj_main
def obj_user_movement(keys_pressed, obj, top=0, left=0, right=0, bottom=0):
    if keys_pressed[pg.K_w] == True and obj.y > bottom:
        obj.y -= VEL[0]
    if keys_pressed[pg.K_s] == True and obj.y < height - top - obj.height:
        obj.y += VEL[0]
    if keys_pressed[pg.K_a] == True and obj.x > right:
        obj.x -= VEL[0]
    if keys_pressed[pg.K_d] == True and obj.x < width - left - obj.width:
        obj.x += VEL[0]


def vell_arr(n=100,m=2):
    VEL_vector = np.ones((n,m))
    VEL_arr = list(VEL_vector)
    for i,np_arr in enumerate(VEL_arr):
        VEL_arr[i] = list(np_arr)

    return VEL_arr

VEL_arr = vell_arr(100)
#print(VEL_arr)

def ai_movement(obj, i:int, velocity:int, top=0, left=0, bottom=0, right=0) -> None:
    obj.x -= VEL_arr[i][0]*velocity
    obj.y -= VEL_arr[i][1]*velocity
    if obj.x < left:
        VEL_arr[i][0] *= -1
        #print(obj.x, obj.y)
    if obj.x > width - right:
        VEL_arr[i][0] *= -1
        #print(obj.x, obj.y)
    if obj.y < top:
        VEL_arr[i][1] *= -1
        #print(obj.x, obj.y)
    if obj.y > height - bottom:
        VEL_arr[i][1] *= -1
        #print(obj.x, obj.y)


def obj_collides(Rect_Object1, Rect_Object2, i1, i2, velocity) -> None:
    if i1 != None and i1 > -1:
        Rect_Object1.move_bot(i1, velocity)
    Rect_Object2.move_bot(i2, velocity)
    if Rect_Object1.top.colliderect(Rect_Object2.bottom):
        if VEL_arr[i2][0] > 0:
            VEL_arr[i2][1] *= -1
            COLOR = (255,0,0)
        elif VEL_arr[i2][0] < 0:
            VEL_arr[i2][1] *= -1
    if Rect_Object1.left.colliderect(Rect_Object2.right):
        if VEL_arr[i2][1] < 0:
            VEL_arr[i2][0] *= -1
            COLOR = (255,0,0)
        elif VEL_arr[i2][1] > 0:
            VEL_arr[i2][0] *= -1
            COLOR = (255,0,0)
    if Rect_Object1.bottom.colliderect(Rect_Object2.top):
        if VEL_arr[i2][0] < 0:
            VEL_arr[i2][1] *= -1
            COLOR = (255,0,0)
        elif VEL_arr[i2][0] > 0:
            VEL_arr[i2][1] *= -1
            COLOR = (255,0,0)
    if Rect_Object1.right.colliderect(Rect_Object2.left):
        if VEL_arr[i2][1] < 0:
            VEL_arr[i2][0] *= -1
            COLOR = (255,0,0)
        elif VEL_arr[i2][1] > 0:
            VEL_arr[i2][0] *= -1
            COLOR = (255,0,0)
