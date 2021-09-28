import tkinter as tk
from .filehandle import *
from tkinter import RIDGE

class ToolFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, height=200, width=160, borderwidth=5, relief=RIDGE)
        self.parent = parent
        self.tool ="click" # set the default tool to the "click" tool for setting tiles
        self.grid(column=0, row=1, sticky = "n") # set to left most column and second row

        self.pointer_img = Tile('images/Pointer.png', 32).image # load cursor icon
        # make a click tool for setting tiles
        self.pointer = tk.Button(self, command = self.click, image = self.pointer_img) 
        self.pointer.pack(side="left")

        self.eraser_img = Tile('images/Eraser.png', 32).image # load eraser icon
        # make an eraser tool for erasing tiles
        self.eraser = tk.Button(self, command = self.eraser, image = self.eraser_img)
        self.eraser.pack(side="right")

    def eraser(self): # set current tool to tile eraser
        self.tool = "erase"

    def click(self): # set current tool to tile setter
        self.tool = "click"
