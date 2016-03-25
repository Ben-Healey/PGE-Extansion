#!/usr/bin/env python

import pge, sys, pygame, time
from Tkinter import *

print "Start Game"
pge.batch ()  # this works


t = pge.rgb (1.0/2.0, 2.0/3.0, 3.0/4.0)
wood_light = pge.rgb (166.0/256.0, 124.0/256.0, 54.0/256.0)
wood_dark = pge.rgb (76.0/256.0, 47.0/256.0, 0.0)
red = pge.rgb (1.0, 0.0, 0.0)
metal = pge.rgb (0.5, 0.5, 0.5)
ball_size = 0.04
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
        self.button1 = Button(self.frame, text = 'Set Number of Objects', width = 40, command = self.Num_window)
        self.button2 = Button(self.frame, text = 'Set Placement of Ball', width=40 ,command = self.Ball_windows)
        self.button3 = Button(self.frame, text = 'Set Points for Each Object ',width = 40, command  = self.Obj_windows) 
        self.button4 = Button(self.frame, text = 'Set Simulation Time', width = 40, command = self.time_windows)
        self.button5 = Button(self.frame, text = 'Continue To Simulation', width = 40, command = self.kill_window)
        self.lab = Label(self.frame, text= "Welcome to the PGE Sandbox!")
        self.lab.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.frame.pack()
        
    def Num_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Num_objects(self.newWindow)
    
    def Ball_windows(self):
        self.newWindow = Toplevel(self.master)
        self.app = Place_Ball(self.newWindow)
    
    def Obj_windows(self):
        self.newWindow = Toplevel(self.master)
        self.app = Obj_Points(self.newWindow)
    
    def time_windows(self):
        self.newWindow = Toplevel(self.master)
        self.app = settime(self.newWindow)
    
    def kill_window(self):
        self.master.destroy()
        
class Num_objects:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Label = Label (self.frame, text = "How many objects would you like to add to the sandbox", width = 50)
        self.Label.pack()
        self.EntryBox = Entry(self.frame)
        self.EntryBox.pack(side = LEFT)
        self.but = Button(self.frame, text = "Done",command = self.close_windows)
        self.but.pack(side = LEFT)
        self.frame.pack()
   
    def close_windows(self):
        global num_objects
        num_objects = int(self.EntryBox.get())
        print num_objects
        self.master.destroy()

    
class Place_Ball:
    
     def __init__(self,master):
        self.master = master
        self.frame = Frame(self.master)
        self.label = Label(self.frame, text = "Please Enter the X, Y and R", width = 50)
        self.label.pack()
        self.label2 = Label(self.frame, text ="X: ")
        self.Entry1 = Entry(self.frame)
        self.label2.pack(side = LEFT)
        self.Entry1.pack(side = LEFT)
        self.label3 = Label(self.frame, text = "Y: ")
        self.Entry2 = Entry(self.frame)
        self.label3.pack(side = LEFT)
        self.Entry2.pack(side = LEFT)
        self.label4 = Label(self.frame, text = "R: ")
        self.Entry3 = Entry(self.frame)
        self.label4.pack(side = LEFT)
        self.Entry3.pack(side = LEFT)
        self.but = Button(self.frame, text = "Done", command = self.close_windows1)
        self.but.pack(side =LEFT)   
        self.frame.pack()
	   #old ball creation no longer needed
       # print(self.Entry1.get())
       # self.firstval.set(self.Entry1.get()) 
       # secval = 0.8
       # thirdval = 0.02
       # c = placeBall (self.firstval, secval, thirdval).mass (1).on_collision (callMe)

     def close_windows1(self):
        print(self.Entry1.get())
        firstval = float(self.Entry1.get()) 
        secval = float(self.Entry2.get())
        thirdval = float(self.Entry3.get()) 
        c = placeBall (firstval, secval, thirdval).mass (1).on_collision (callMe)
        self.master.destroy()
        
class Obj_Points:
    def __init__(self,master):
       if num_objects == 1:
          obj1(self, master)
       else:
          print("NOT COMPLETE!")          
    def obj1(self,master):
       self.master = master
       self.frame = Frame(self.master)
       self.label = Label(self.frame, text = "Please Enter X, Y and R", width = 50)
       self.label.pack()
       self.frame.pack()

class settime:
    def __init__(self,master):
        self.master = master
        self.frame = Frame(self.master)
        self.label = Label(self.frame, text= "Set Simulation Time in Seconds", width= 50)
        self.label.pack()
        self.EntryT = Entry(self.frame)
        self.EntryT.pack()
        self.but = Button(self.frame, text = "Done ", command = self.sett)
        self.but.pack()
        self.frame.pack()
                          
    def sett(self):
        global time
        time = float(self.EntryT.get())
        print time
        self.master.destroy()
                    

def main ():
    
    master = Tk()
  
    master.title("PGE-Sandbox")
    print "About to run window"
    app = wind1(master)
    master.mainloop()
    #c = placeBall (0.55, 0.8, 0.02).mass (1).on_collision (callMe)
    #l = placeBox ([0.3, 0.3], [0.3, 0.5], [0.5, 0.5], [0.5, 0.3])
        #Own code 
   # l2 = placeBox ([0.55, 0.55], [0.0, 0.0], [0.80, 0.80], [0.8, 0.2])
    #l3 = placeBox ([0.15, 0.15], [0.25, 0.25], [0.03, 0.03], [0.02, 0.8])
    b1, b2, b3, b4 = placeBoarders (boarder, wood_light)
    print "before run"
    pge.gravity ()
    pge.dump_world ()
    pge.run (time)
    pge.finish ()
    
print "before main()"
main ()

