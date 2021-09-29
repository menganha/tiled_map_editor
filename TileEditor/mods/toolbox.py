 #   This file is part of Tile Basic
 #   Copyright (C) 2021  @Multilingual-Coder

#    Tile Basic is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Tile Basic is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#    
#    Contact the developer at codermultilingual@gmail.com
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
