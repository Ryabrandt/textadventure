#TextAdventure
#Working Title: The Wailing Mountain: The Quest to Defeat the Dragon 

from Tkinter import *
import sys
from character import *
from rooms import *
from rooms2 import *
from rooms3 import *
#####
# Textbox source code is from http://codingmess.blogspot.com/2008/08/text-box-with-scrollbar.html
""" 
class TxtboxOut(object):
    def __init__(self, tkintertxt):
        self.T = tkintertxt
 
    def write(self, txt):
        self.T.insert(Tkinter.END, "%s" % str(txt))
        self.T.yview(Tkinter.MOVETO, 1.0)
 
root = Tkinter.Tk()
s = Tkinter.Scrollbar(root)
T = Tkinter.Text(root)
newout = TxtboxOut(T)
console = sys.stdout
sys.stdout = newout
 
T.focus_set()
s.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
T.pack(side=Tkinter.LEFT, fill=Tkinter.Y)
s.config(command=T.yview)
T.config(yscrollcommand=s.set)

#Tkinter.mainloop()
"""
#####
"""
def textHandler():
    pass
def monsterHandler():
    pass
def inventoryHandler():
    pass
"""
def mousePressed(event):
    redrawAll()

def keyPressed(event):
    redrawAll()
"""
def drawGameOverScreen():
    pass
def drawOpeningScreen():
    redrawALL()

def drawStats():
    pass
def drawInventory():
    pass
def drawMonster():
    pass
5def drawUI():
    image = canvas.data.image
    imageSize = ( (image.width(), image.height()) )
    canvas.create_image(0,0,anchor=N, image=image)
    
def redrawAll():
    canvas.delete(ALL)
    drawUI()
"""
def init():
    #canvas.width = canvas.winfo_reqwidth()-4
    #canvas.height = canvas.winfo_reqheight()-4
    #canvas.data.image = PhotoImage(file="TermProjectInterface.gif")
    canvas.data.inventoryList = [["apple"]]
    canvas.data.XP = 0
    canvas.data.hp = 0
    canvas.data.dp = 0
    canvas.data.gold = getStartingGold(canvas)
    canvas.data.monster = "none"
    canvas.data.monsterHP = 0
    canvas.data.monsterDP = 0
    canvas.data.monsterGold = 0
    canvas.data.monsterLives = 0
    canvas.data.monster2Lives = 0
    canvas.data.torchInUse = False
    canvas.data.visited1a = False
    canvas.data.visited1b = False
    canvas.data.visited2a = False
    canvas.data.visited2b = False
    canvas.data.visited3a = False
    canvas.data.visited3b = False
    canvas.data.visited4a = False
    canvas.data.visited4b = False
    canvas.data.visited4c = False
    canvas.data.visited5a = False
    canvas.data.visited5b = False
    canvas.data.visited5d = False
    canvas.data.visited6a = False
    canvas.data.visited6d = False
    canvas.data.gameOver = False
    openingScreen(canvas)

    
########### copy-paste below here ###########

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
