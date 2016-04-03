#!/usr/bin/env python

import pge, sys, pygame, time, config
from Tkinter import *

print "Start Game"
pge.batch ()


t = pge.rgb (1.0/2.0, 2.0/3.0, 3.0/4.0)
wood_light = pge.rgb (166.0/256.0, 124.0/256.0, 54.0/256.0)
wood_dark = pge.rgb (76.0/256.0, 47.0/256.0, 0.0)
red = pge.rgb (1.0, 0.0, 0.0)
metal = pge.rgb (0.5, 0.5, 0.5)
ball_size = 0.04
boarder = 0.001
white = pge.rgb (1.0, 0.0, 1.0)
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
        self.button2 = Button(self.frame, text = 'Set Points for Each Object ',width = 40, command  = self.Obj_windows) 
        self.button3 = Button(self.frame, text = 'Set Placement of Ball', width=40 ,command = self.Ball_windows) 
        self.button4 = Button(self.frame, text = 'Set Simulation Time', width = 40, command = self.time_windows)
        self.button5 = Button(self.frame, text = 'Continue To Simulation', width = 40, command = self.kill_window)
        self.lab = Label(self.frame, text= "Welcome to the PGE Sandbox!")
        self.lab.grid()
        self.button1.grid()
        self.button2.grid()
        self.button3.grid()
        self.button4.grid()
        self.button5.grid()
        self.frame.grid()
        print "Ball Boolean: "
        print config.Ball
        print "Number of Objects Boolean: "
        print config.NumObjects
        print "Object Points Boolean: "
        print config.ObjectPoints
        print "Simulation Time Boolean: "
        print config.SimTime
    def Num_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Num_Objects(self.newWindow)
    
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
        if config.Ball == True and config.NumObjects == True and config.ObjectPoints == True and config.SimTime == True:
         self.master.destroy()
        else:
         print "Didnt Work"
         self.newWindow = Toplevel(self.master)
         self.app = Error(self.newWindow)

class Num_Objects:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.Label = Label (self.frame, text = "How many objects would you like to add to the sandbox (1-4)", width = 49)
        self.EntryBox = Entry(self.frame)
        self.but = Button(self.frame, text = "Done",command = self.close_windows)
        self.Label.grid(column = 0)
        self.EntryBox.grid(row = 1, column = 0,columnspan = 3 ,sticky = W)
        self.but.grid(row = 1, column = 0, sticky=E)
        self.frame.grid()
   
    def close_windows(self):
        config.NumObjects = True
        config.Num_Objects = int(self.EntryBox.get())
        print config.Num_Objects
        self.master.destroy()

    
class Place_Ball:
    
     def __init__(self,master):
        self.master = master
        self.frame = Frame(self.master)
        self.label = Label(self.frame, text = "Please Enter the X, Y and R:", width = 50)
        self.label.grid(columnspan = 2, sticky = W+E)
        self.label2 = Label(self.frame, text ="X:")
        self.Entry1 = Entry(self.frame)
        self.label2.grid(row = 2, sticky = W+E)
        self.Entry1.grid(row = 2, column = 1)
        self.label3 = Label(self.frame, text = "Y:")
        self.Entry2 = Entry(self.frame)
        self.label3.grid(row = 3, sticky = W+E)
        self.Entry2.grid(row = 3, column = 1)
        self.label4 = Label(self.frame, text = "R:")
        self.Entry3 = Entry(self.frame)
        self.label4.grid(row = 4, sticky = W+E)
        self.Entry3.grid(row = 4, column = 1)
        self.but = Button(self.frame, text = "Done", command = self.close_windows1)
        self.but.grid(row = 5,columnspan = 2, sticky = W+E)   
        self.frame.grid()

     def close_windows1(self):
        config.Ball = True
        print config.Ball
        print(self.Entry1.get())
        Xval = float(self.Entry1.get()) 
        Yval = float(self.Entry2.get())
        Rval = float(self.Entry3.get()) 
        c = placeBall (Xval, Yval, Rval).mass (1).on_collision (callMe)
        self.master.destroy()
        
class Obj_Points:

    def __init__(self,master):
       if config.Num_Objects >= 1 and config.Num_Objects <= 4:
          self.master = master
          self.frame = Frame(self.master)
          self.label = Label(self.frame, text = "Please Enter Four Points for the Object", width = 50)
          self.label.grid(columnspan = 3)
          #Start of first point
          self.label2 = Label(self.frame, text = "First point(X,Y) : ")
          self.label2.grid(row = 2, sticky = W+E)
          self.Entry1 = Entry(self.frame)
          self.Entry1.grid(row = 2, column = 1)
          self.Entry2 = Entry(self.frame)
          self.Entry2.grid(row = 2, column = 2)
          #Start of Second point
          self.label3 = Label(self.frame, text = "Second Point(X,Y) : ")
          self.label3.grid(row = 3)
          self.Entry3 = Entry(self.frame)
          self.Entry3.grid(row = 3, column = 1)
          self.Entry4 = Entry(self.frame)
          self.Entry4.grid(row = 3, column = 2)
          #Start of third point
          self.label4 = Label(self.frame, text = "Third Point(X,Y) : ")
          self.label4.grid(row = 4)
          self.Entry5 = Entry(self.frame)
          self.Entry5.grid(row = 4, column = 1)
          self.Entry6 = Entry(self.frame)
          self.Entry6.grid(row = 4, column = 2)
          #start of fourth point
          self.label5 = Label(self.frame, text = "Fourth Point(X,Y) : ")
          self.label5.grid(row = 5)
          self.Entry7 = Entry(self.frame)
          self.Entry7.grid(row = 5, column = 1)
          self.Entry8 = Entry(self.frame)
          self.Entry8.grid(row = 5, column = 2) 
          if config.Num_Objects == 1:
            self.button = Button(self.frame, text = "Done", command = self.close)
          else:
             self.button = Button(self.frame, text = "Done", command = self.Sec)
          
          self.button.grid(row = 6,columnspan = 3, sticky = W + E)
          self.frame.grid()
       else:
          self.master = master
          self.frame = Frame(self.master)
          self.label = Label(self.frame, text = "Invalid or No Number Has Been Inputted")
          self.label.grid()
          self.button = Button(self.frame, text = "Done", command =  self.close)
          self.button.grid()
          self.frame.grid()

    def close(self):
      config.ObjectPoints = True
      if config.Num_Objects == 1:
        x1 = float(self.Entry1.get())
        y1 = float(self.Entry2.get())
        x2 = float(self.Entry3.get())
        y2 = float(self.Entry4.get())
        x3 = float(self.Entry5.get())
        y3 = float(self.Entry6.get())
        x4 = float(self.Entry7.get())
        y4 = float(self.Entry8.get())
        t = placeBox([x1,y1],[x2,y2],[x3,y3],[x4,y4])
        self.master.destroy()
      elif config.Num_Objects == 2:
        #first object
        x1 = float(self.Entry1.get())
        y1 = float(self.Entry2.get())
        x2 = float(self.Entry3.get())
        y2 = float(self.Entry4.get())
        x3 = float(self.Entry5.get())
        y3 = float(self.Entry6.get())
        x4 = float(self.Entry7.get())
        y4 = float(self.Entry8.get())
        t = placeBox([x1,y1],[x2,y2],[x3,y3],[x4,y4])
        #second object
        x12 = float(self.En1.get())
        y12 = float(self.En2.get())
        x22 = float(self.En3.get())
        y22 = float(self.En4.get())
        x32 = float(self.En5.get())
        y32 = float(self.En6.get())
        x42 = float(self.En7.get())
        y42 = float(self.En8.get())
        t2 = placeBox([x12,y12],[x22,y22],[x32,y32],[x42,y42])
        self.master.destroy()
      elif config.Num_Objects == 3:
        #first object
        x1 = float(self.Entry1.get())
        y1 = float(self.Entry2.get())
        x2 = float(self.Entry3.get())
        y2 = float(self.Entry4.get())
        x3 = float(self.Entry5.get())
        y3 = float(self.Entry6.get())
        x4 = float(self.Entry7.get())
        y4 = float(self.Entry8.get())
        t = placeBox([x1,y1],[x2,y2],[x3,y3],[x4,y4])
        #second object
        x12 = float(self.En1.get())
        y12 = float(self.En2.get())
        x22 = float(self.En3.get())
        y22 = float(self.En4.get())
        x32 = float(self.En5.get())
        y32 = float(self.En6.get())
        x42 = float(self.En7.get())
        y42 = float(self.En8.get())
        t2 = placeBox([x12,y12],[x22,y22],[x32,y32],[x42,y42])
        #third object
        x13 = float(self.Ent1.get())
        y13 = float(self.Ent2.get())
        x23 = float(self.Ent3.get())
        y23 = float(self.Ent4.get())
        x33 = float(self.Ent5.get())
        y33 = float(self.Ent6.get())
        x43 = float(self.Ent7.get())
        y43 = float(self.Ent8.get())
        t3 = placeBox([x13,y13],[x23,y23],[x33,y33],[x43,y43])
        self.master.destroy()
      elif config.Num_Objects == 4:
        #first object
        x1 = float(self.Entry1.get())
        y1 = float(self.Entry2.get())
        x2 = float(self.Entry3.get())
        y2 = float(self.Entry4.get())
        x3 = float(self.Entry5.get())
        y3 = float(self.Entry6.get())
        x4 = float(self.Entry7.get())
        y4 = float(self.Entry8.get())
        t = placeBox([x1,y1],[x2,y2],[x3,y3],[x4,y4])
        #second object
        x12 = float(self.En1.get())
        y12 = float(self.En2.get())
        x22 = float(self.En3.get())
        y22 = float(self.En4.get())
        x32 = float(self.En5.get())
        y32 = float(self.En6.get())
        x42 = float(self.En7.get())
        y42 = float(self.En8.get())
        t2 = placeBox([x12,y12],[x22,y22],[x32,y32],[x42,y42])
        #third object
        x13 = float(self.Ent1.get())
        y13 = float(self.Ent2.get())
        x23 = float(self.Ent3.get())
        y23 = float(self.Ent4.get())
        x33 = float(self.Ent5.get())
        y33 = float(self.Ent6.get())
        x43 = float(self.Ent7.get())
        y43 = float(self.Ent8.get())
        t3 = placeBox([x13,y13],[x23,y23],[x33,y33],[x43,y43])
        #fourth object
        x14 = float(self.E1.get())
        y14 = float(self.E2.get())
        x24 = float(self.E3.get())
        y24 = float(self.E4.get())
        x34 = float(self.E5.get())
        y34 = float(self.E6.get())
        x44 = float(self.E7.get())
        y44 = float(self.E8.get())
        t4 = placeBox([x14,y14],[x24,y24],[x34,y34],[x44,y44])
        self.master.destroy()
      elif (config.Num_Objects == 0) or (config.Num_Objects >= 5):
        self.master.destroy()

    def Sec(self):
         self.frame.grid_forget()
         self.frame = Frame(self.master)
         self.label = Label(self.frame, text = "Please Enter The Second Objects Four Points", width = 50)
         self.label.grid(columnspan = 3)
         #Start of second point
         self.label2 = Label(self.frame, text = "First Point (X,Y) : ")
         self.label2.grid(row = 2, sticky =W +E)
         self.En1 = Entry(self.frame)
         self.En1.grid(row = 2, column = 1)
         self.En2 = Entry(self.frame)
         self.En2.grid(row = 2, column = 2)
         #Start of second point
         self.label3 = Label(self.frame, text = "Second Point(X,Y) : ")
         self.label3.grid(row = 3, sticky =W +E)
         self.En3 = Entry(self.frame)
         self.En3.grid(row = 3, column = 1)
         self.En4 = Entry(self.frame)
         self.En4.grid(row = 3, column = 2)
         #Start of third point
         self.label4 = Label(self.frame, text = "Third Point(X,Y) : ")
         self.label4.grid(row = 4, sticky =W +E)
         self.En5 = Entry(self.frame)
         self.En5.grid(row = 4, column = 1)
         self.En6 = Entry(self.frame)
         self.En6.grid(row = 4, column = 2)
         #Start of Fourth point
         self.label5 = Label(self.frame, text = "Fourth Point(X,Y) : ")
         self.label5.grid(row = 5, sticky =W +E)
         self.En7 = Entry(self.frame)
         self.En7.grid(row = 5, column = 1)
         self.En8 = Entry(self.frame)
         self.En8.grid(row = 5, column = 2)
      
         if config.Num_Objects == 2:
             self.button = Button(self.frame, text = "Done", command =  self.close)
         else:
              self.button = Button(self.frame, text = "Done", command =  self.third)   
         
         self.button.grid(columnspan = 3,sticky = W +E)
         self.frame.grid()

    def third(self):
         self.frame.grid_forget()
         self.frame = Frame(self.master)
         self.label = Label(self.frame, text = "Please Enter The Third Objects Four Points", width = 50)
         self.label.grid(columnspan = 3)
         #Start of second point
         self.label2 = Label(self.frame, text = "First Point (X,Y) : ")
         self.label2.grid(row = 2, sticky =W +E)
         self.Ent1 = Entry(self.frame)
         self.Ent1.grid(row = 2, column = 1)
         self.Ent2 = Entry(self.frame)
         self.Ent2.grid(row = 2, column = 2)
         #Start of second point
         self.label3 = Label(self.frame, text = "Second Point(X,Y) : ")
         self.label3.grid(row = 3, sticky =W +E)
         self.Ent3 = Entry(self.frame)
         self.Ent3.grid(row = 3, column = 1)
         self.Ent4 = Entry(self.frame)
         self.Ent4.grid(row = 3, column = 2)
         #Start of third point
         self.label4 = Label(self.frame, text = "Third Point(X,Y) : ")
         self.label4.grid(row = 4, sticky =W +E)
         self.Ent5 = Entry(self.frame)
         self.Ent5.grid(row = 4, column = 1)
         self.Ent6 = Entry(self.frame)
         self.Ent6.grid(row = 4, column = 2)
         #Start of Fourth point
         self.label5 = Label(self.frame, text = "Fourth Point(X,Y) : ")
         self.label5.grid(row = 5, sticky =W +E)
         self.Ent7 = Entry(self.frame)
         self.Ent7.grid(row = 5, column = 1)
         self.Ent8 = Entry(self.frame)
         self.Ent8.grid(row = 5, column = 2)
      
         if config.Num_Objects == 3:
             self.button = Button(self.frame, text = "Done", command =  self.close)
         else:
              self.button = Button(self.frame, text = "Done", command =  self.fourth)   
         
         self.button.grid(columnspan = 3,sticky = W +E)
         self.frame.grid()
         
    def fourth(self):
         self.frame.grid_forget()
         self.frame = Frame(self.master)
         self.label = Label(self.frame, text = "Please Enter The Fourth Objects Four Points", width = 50)
         self.label.grid(columnspan = 3)
         #Start of second point
         self.label2 = Label(self.frame, text = "First Point (X,Y) : ")
         self.label2.grid(row = 2, sticky =W +E)
         self.E1 = Entry(self.frame)
         self.E1.grid(row = 2, column = 1)
         self.E2 = Entry(self.frame)
         self.E2.grid(row = 2, column = 2)
         #Start of second point
         self.label3 = Label(self.frame, text = "Second Point(X,Y) : ")
         self.label3.grid(row = 3, sticky =W +E)
         self.E3 = Entry(self.frame)
         self.E3.grid(row = 3, column = 1)
         self.E4 = Entry(self.frame)
         self.E4.grid(row = 3, column = 2)
         #Start of third point
         self.label4 = Label(self.frame, text = "Third Point(X,Y) : ")
         self.label4.grid(row = 4, sticky =W +E)
         self.E5 = Entry(self.frame)
         self.E5.grid(row = 4, column = 1)
         self.E6 = Entry(self.frame)
         self.E6.grid(row = 4, column = 2)
         #Start of Fourth point
         self.label5 = Label(self.frame, text = "Fourth Point(X,Y) : ")
         self.label5.grid(row = 5, sticky =W +E)
         self.E7 = Entry(self.frame)
         self.E7.grid(row = 5, column = 1)
         self.E8 = Entry(self.frame)
         self.E8.grid(row = 5, column = 2)
         self.button = Button(self.frame, text = "Done", command =  self.close)
         self.button.grid(columnspan = 3,sticky = W +E)
         self.frame.grid()
class settime:
    def __init__(self,master):
        self.master = master
        self.frame = Frame(self.master)
        self.label = Label(self.frame, text= "Set Simulation Time (In Seconds)")
        self.label.grid(row = 1, columnspan = 2)
        self.EntryT = Entry(self.frame)
        self.EntryT.grid(row = 2,sticky =W)
        self.but = Button(self.frame, text = "Done ", command = self.sett)
        self.but.grid(row = 2, column = 1)
        self.frame.grid()
                          
    def sett(self):
        config.SimTime = True
        config.Time = float(self.EntryT.get())
        print config.Time
        self.master.destroy()

class Error:
   def __init__(self,master):
        self.master = master
        self.frame = Frame(self.master)
        self.Error = Label(self.frame, text = "Error, No or Only Parital Parameters are Inputted", width = 40)
        self.Error.grid()
        self.button = Button(self.frame,text = "OK", width = 40, command = self.close)
        self.button.grid()
        self.frame.grid()
    
   def close(self):
        self.master.destroy()   

def main ():
    
    master = Tk()
  
    master.title("PGE-Sandbox")
    print "About to run window"
    app = wind1(master)
    master.mainloop()
   





    b1, b2, b3, b4 = placeBoarders (boarder, wood_light)
    print "before run"
    pge.gravity ()
    pge.dump_world ()
    pge.run (config.Time)
    pge.finish ()
    
print "before main()"
main ()

