  #   This file is part of Tile Basic
 #   Copyright (C) 2021-2022  @Multilingual-Coder
 #   Copyright (C) 2022 Bill Roberts

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
        self.boxstart = [] #variable that holds the position of the topmost corner of a selection box.
        self.boxend = [] #variable that holds the position of the bottommost corner of the selection box.
        self.grid(column=0, row=1, sticky = "n") # set to left most column and second row

        self.pointer_img = Tile('images/Pointer.png', 32).image # load cursor icon
        # make a click tool for setting tiles
        self.pointer = tk.Button(self, command = self.click, image = self.pointer_img) 
        self.pointer.pack(side="left")

        #make a boxSelect tool for setting multiple tiles at once
        self.boxselect_img = Tile('images/boxSelect.png',32).image # load boxSelect icon

        self.boxselect = tk.Button(self, command = self.boxselect, image = self.boxselect_img)
        self.boxselect.pack(side = "bottom")

        self.eraser_img = Tile('images/Eraser.png', 32).image # load eraser icon
        # make an eraser tool for erasing tiles
        self.eraser = tk.Button(self, command = self.eraser, image = self.eraser_img)
        self.eraser.pack(side="right")
        self.click() # set default tool to 'click'

    def eraser(self):
        self.tool = "erase"
        # Set the Eraser button image to 'active'
        self.imgE = tk.PhotoImage(file='images/EraserActive.png')
        self.eraser.config(image=self.imgE)
        # Set the Pointer button image to 'inactive'
        self.imgP = tk.PhotoImage(file='images/Pointer.png')
        self.pointer.config(image=self.imgP)
        # Set the boxSelect image to 'inactive'
        self.imgB = tk.PhotoImage(file='images/boxSelect.png')
        self.boxselect.config(image=self.imgB)

    def click(self):
        self.tool = "click"
        # Set the Eraser button image to 'inactive'
        self.imgE = tk.PhotoImage(file='images/Eraser.png')
        self.eraser.config(image=self.imgE)
        # Set the boxSelect image to 'inactive'
        self.imgB = tk.PhotoImage(file='images/boxSelect.png')
        self.boxselect.config(image=self.imgB)
        # Set the Pointer button image to 'active'
        self.imgP = tk.PhotoImage(file='images/PointerActive.png')
        self.pointer.config(image=self.imgP)

    def boxselect(self):
        self.tool = "boxselect"
        # Set the Pointer button image to 'inactive'
        self.imgP = tk.PhotoImage(file='images/Pointer.png')
        self.pointer.config(image=self.imgP)
        # Set the Eraser button to 'inactive'
        self.imgE = tk.PhotoImage(file='images/Eraser.png')
        self.eraser.config(image=self.imgE)
        # Set the boxSelect image to 'active'
        self.imgB = tk.PhotoImage(file='images/boxSelectActive.png')
        self.boxselect.config(image=self.imgB)
