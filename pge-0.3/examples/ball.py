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


    
    
    
class wind1:
    
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.button1 = Button(self.frame, text = 'Set Number of Objects', width = 40, command = self.new_window)
        self.button2 = Button(self.frame, text = 'Set Placement of Ball', width=40 ,command = self.new_window)
        self.button3 = Button(self.frame, text = 'Set Points for Each Object ',width = 40, command  = self.new_window) 
        self.button4 = Button(self.frame, text = 'Set Simulation Time', width = 40, command = self.new_window)
        self.button5 = Button(self.frame, text = 'Continue To Simulation', width = 40, command = self.new_window)
        self.lab = Label(self.frame, text= "Welcome to the PGE Sandbox")
        self.lab.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.frame.pack()
        
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Num_objects(self.newWindow)
 
    
class Num_objects:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Label = Label (self.frame, text = "How many objects would you like to add to the sandbox", width = 50)
        self.Label.pack()
        self.EntryBox = Entry(self.frame)
        self.EntryBox.pack(side = LEFT)
        self.but = Button(self.frame, text = "Done",command = self.close_windows)
        self.but.pack()
        self.frame.pack()
    def close_windows(self):
        print self.EntryBox.get()
        self.master.destroy()
        
    def getval(self):
        self.EntryBox.get()

    


#def used to close window
#def quit():
 #   print "Quit"
  #  root.quit()
    
#def test2():
 #       val = test.get()
    
  #      try:
   #         val = float(val)
    #        print val
     #   except ValueError:
      #      print "Bad Input"
        
       # root.quit()
        #Button(text="Test", command=test2).grid()
    
def main ():

    master = Tk()
    
    #var = StringVar()
    #var2 = StringVar()
    #label = Button( root, textvariable=var, relief=FLAT,command = quit)
    #var.set("Welcome to the PGE Sandpit! Click me to continue")
    #root.geometry("200x200")
    #label.pack()
    master.title("PGE-Sandbox")
    print "About to run window"
    app = wind1(master)
    master.mainloop()
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
