#Electric field mapper | George Gearing | 21/08/2020 (Redo due to laptop crashing)
from tkinter import *
from math import sqrt

SCALE=10
WIDTH=2000
HEIGHT=1000
K=8987551788
class Charge:
    def __init__(self,x,y,q):
        self.x=x
        self.y=y
        self.q=q

    def getPosition(self):
        return (self.x,self.y)

    def getCharge(self):
        return self.q

    def getColour(self):
        if self.q<0:
            return "red"
        else:
            return "green"
        
    def getRadius(self):
        return self.q*SCALE

    
class ElectricField:
    def __init__(self,Ex=0,Ey=0):
        self.Ex=Ex
        self.Ey=Ey
        

        
    def getFieldStrength(self):
        return sqrt(self.Ex**2+self.Ey**2)
    
    def getField(self):
        return (self.Ex,self.Ey)
    
    def add(self,field):
        ex,ey=field.getField()
        self.Ex+=ex
        self.Ey+=ey
        

    
def loadCharges(filename):
    chargeList=list()
    f = open(filename, "r")
    lines=f.read().split(";")
    for i in range(len(lines)):
        current=lines[i].split(",")
        chargeList.append(Charge(float(current[0]),float(current[1]),float(current[2])))
    return chargeList

def getFieldStrength(chargeList,x,y):
    E=ElectricField()
    for i in range(len(chargeList)):
        current=chargeList[i]
        xi,yi=current.getPosition()
        Rx=x-xi
        Ry=y-yi
        mag=(K*current.getCharge())/(sqrt(Rx**2+Ry**2))**3
        Ei=ElectricField(mag*Rx,mag*Ry)
        E.add(Ei)
    return E
window=Tk()
c = Canvas(window, width=WIDTH, height=HEIGHT)
c.pack()
charges=loadCharges("charges.txt")

for i in range(len(charges)):
    x,y=charges[i].getPosition()
    r=charges[i].getRadius()
    c.create_oval(x-r,y-r,x+r,y+r,fill=charges[i].getColour())
    

#Testing area:
spacing=20
for x in range(1,WIDTH,spacing):
    for y in range(1,HEIGHT,spacing):
        
        scale=10000
        E=getFieldStrength(charges,x,y)
        Ex,Ey=E.getField()
        mag=E.getFieldStrength()
        line=c.create_line(x,y,x+Ex/scale,y+Ey/scale,arrow=LAST)


