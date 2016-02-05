#!/usr/bin/env python

import pge, sys, pygame, easygui
from Tkinter import *


print "Start Game"
pge.batch ()  # this works
# pge.interactive () # and this fails (the code is incomplete)

t = pge.rgb (1.0/2.0, 2.0/3.0, 3.0/4.0)
wood_light = pge.rgb (166.0/256.0, 124.0/256.0, 54.0/256.0)
wood_dark = pge.rgb (76.0/256.0, 47.0/256.0, 0.0)
red = pge.rgb (1.0, 0.0, 0.0)
metal = pge.rgb (0.5, 0.5, 0.5)
ball_size = 0.004
boarder = 0.001
white = pge.rgb (1.0, 1.0, 1.0)
gap = 0.01


def placeBoarders (thickness, color):
    print "placeBoarders"
    e1 = pge.box (0.0, 0.0, 1.0, thickness, color).fix ()
    e2 = pge.box (0.0, 0.0, thickness, 1.0, color).fix ()
    e3 = pge.box (1.0-thickness, 0.0, thickness, 1.0, color).fix ()
    e4 = pge.box (0.0, 1.0-thickness, 1.0, thickness, color).fix ()
    return e1, e2, e3, e4

def placeBall (x, y, r):
    return pge.circle (x, y, r, metal)


def placeBox (p0, p1, p2, p3):
    t = pge.poly4 (p0[0], p0[1], p1[0], p1[1],
                   p2[0], p2[1], p3[0], p3[1], white)
    t.fix ()

def callMe (p):
    print "box has collided!"

root = Tk()
def quit():
    print "Quit"
    root.quit()
    
def main ():

    #root = Tk()

    var = StringVar()
    label = Button( root, textvariable=var, relief=FLAT,command = quit)
    var.set("Welcome to the PGE Sandpit!")
    #root.geometry("200x200")
    label.pack()

    root.mainloop()
    c = placeBall (0.55, 0.8, 0.02).mass (1).on_collision (callMe)
    l = placeBox ([0.3, 0.3], [0.3, 0.5], [0.5, 0.5], [0.5, 0.3])
        #Own code 
    l2 = placeBox ([0.55, 0.55], [0.0, 0.0], [0.80, 0.80], [0.8, 0.2])
    l3 = placeBox ([0.15, 0.15], [0.25, 0.25], [0.03, 0.03], [0.02, 0.8])
    
    b1, b2, b3, b4 = placeBoarders (boarder, wood_light)
    print "before run"
    pge.gravity ()
    pge.dump_world ()
    pge.run (5.0)
    pge.finish ()
    

print "before main()"
main ()
