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
from textwrap import fill
import tkinter as tk
from tkinter import RIDGE

class CanvasFrame(tk.Frame): #Frame is created on the window.  Frame then creates canvas in it
    def __init__(self, parent, title):
        tk.Frame.__init__(self, parent)
        self.parent = parent # allows access to the canvas frame's parent (main window)
        self.w = (self.parent.winfo_screenwidth() - 170) * 0.75 # the width of the canvas...
        self.h = (self.parent.winfo_screenheight()) * 0.75 #...is 75% of the available screen space
        self["relief"] = RIDGE #creates a raised area around the canvas frame
        self["width"] = self.w
        self["height"] = self.h
        self["borderwidth"] = 5
        self.ybar = tk.Scrollbar(self,orient="vertical") #make a vertical scrollbar
        self.xbar = tk.Scrollbar(self,orient="horizontal") #make a horizontal scrollbar
        self.cmap = CanvasMap(self, title) # create the grid-map that will hold the tiles and pass the title argument to it
        self.ybar["command"] = self.cmap.yview #set the scrollbar to change the "y" area seen on canvas
        self.xbar["command"] = self.cmap.xview #set the scrollbar to change the "x" area seen on canvas
        self.ybar.grid(column=1,row=0,sticky="ns") #make scrollbar span the distance of the canvas frame
        self.xbar.grid(column=0,row=1,sticky="ew") #make scrollbar span the distance of the canvas frame
        # sets the padding region to 10% of the available space left.
        self.grid(row=0, column=1, padx=(self.parent.winfo_screenwidth() - 170) * 0.1 ,
                 pady=20, rowspan=2) #Adding rowspan=2 allows the canvas to take up two rows
class CanvasMap(tk.Canvas):
    def __init__(self, parent, title):
        tk.Canvas.__init__(self, parent)
        self.parent = parent # allows access to the canva's parent (canvas frame)
        self.w = self.parent.w # sets width and height of canvas to that of canvas frame
        self.h = self.parent.h 
        self.title = title
        self["bg"] = "#2e2e2e" #makes a dark grey color
        self["width"] = self.w #sets size of percivable area of canvas to the parent frame's size
        self["height"] = self.h
        self["yscrollcommand"] = self.parent.ybar.set #gives y scrolling autority to the y scrollbar
        self["xscrollcommand"] = self.parent.xbar.set #gives x scrolling autority to the x scrollbar
        self["scrollregion"] = (0,0,4000,4000) #makes a large scrolling area of canvas
        self.xview_moveto("0.0") #set x scroll to left of canvas
        self.yview_moveto("0.0") #set y scroll to top of canvas
        self.tsize = 32
        self.bind("<Button-1>", self.selectTile)
        self.bind("<B1-Motion>", self.selectTile)
        self.bind("<ButtonRelease-1>", self.boxSelect)
        #create a list of lines spanning the canvas
        for i in range(int(4000 / self.tsize) + 1): # add extra line so we don't miss a column
            self.create_line(i * self.tsize, 0, i * self.tsize, 4000, fill="light grey") #draw vert line
        for i in range(int(4000 / self.tsize) + 1): # add extra line so we don't miss a row
            self.create_line(0, i * self.tsize, 4000, i * self.tsize, fill="light grey") #draw horiz line
        self.grid(column=0,row=0) #puts the canvas on the canvas frame

    def selectTile(self, event):
        self.parent.parent.saved = False
        a = self.parent.xbar.get()[0] # the position of the left side of the horizontal scrollbar
        b = self.parent.ybar.get()[0] # the position of the bottom side of the vertical scrollbar
        #changes the clicked position on the canvas to a position on the map as a whole
        self.tilepos = (int((a * 4000 + event.x) / self.tsize), int((b * 4000 + event.y) / self.tsize)) #finds the number of the tile that our click falls inside
        
        self.setTile()

    def setTile(self):
        tm = self.parent.parent.tmap #easy reference to the entire tilemap array
        if self.parent.parent.tbox.tool == "click":
            img = self.parent.parent.ibox.currentImage #easy reference to the current selected image
            path = self.parent.parent.ibox.currentImagePath

            if tm.canvasarray [self.tilepos[1]] [self.tilepos[0]] != " ": #if a tile is already in the position we clicked
                self.delete(tm.canvasarray [self.tilepos[1]] [self.tilepos[0]]) #...delete it
            #draw the selected tile on the canvas at the clicked position
            canimg = self.create_image(self.tilepos[0] * self.tsize, self.tilepos[1] * self.tsize, image=img, anchor = tk.NW)
            tm.tilearray [self.tilepos[1]] [self.tilepos[0]] = path
            tm.canvasarray [self.tilepos[1]] [self.tilepos[0]] = canimg
            # ...and a canvas compatible image to another array.

        if self.parent.parent.tbox.tool == "erase":
            self.delete(tm.canvasarray [self.tilepos[1]] [self.tilepos[0]]) #erase tile
            tm.canvasarray [self.tilepos[1]] [self.tilepos[0]] = ' ' #forget tile from canvas array
            tm.tilearray [self.tilepos[1]] [self.tilepos[0]] = ' ' #remove tile from tilemap

        if self.parent.parent.tbox.tool == "boxselect":
            if self.parent.parent.tbox.boxstart == []: #if there is not a selection box being drawn...
                self.parent.parent.tbox.boxstart = [self.tilepos[0], self.tilepos[1]] #...hold the top corner of a new one
            else:
                try:
                    self.delete(self.rect) # delete the selection box
                except:
                    pass
                #draws a selection rectangle that will be filled with tiles
                self.rect = self.create_rectangle(self.parent.parent.tbox.boxstart[0] * self.tsize, self.parent.parent.tbox.boxstart[1] * self.tsize, self.tilepos[0] * self.tsize, self.tilepos[1] * self.tsize, dash=(5,5), outline="black")


        self.title('Tile Basic (column: ' + str(self.tilepos[0]+1) +
                    ', row: ' + str( self.tilepos[1]+1) + ')')

    def boxSelect(self, event):
        if self.parent.parent.tbox.tool == "boxselect":
            bxst = self.parent.parent.tbox.boxstart # easy reference to the starting corner of the selection box
            self.delete(self.rect)
            for i in range(abs(bxst[0] - self.tilepos[0])): # loop through all possible positions inside the selection box
                for j in range(abs(bxst[1] - self.tilepos[1])):
                    if bxst[0] > self.tilepos[0]: # make sure that the interior of the selection box is being filled
                        if bxst[1] > self.tilepos[1]:
                            self.fillBox(i, j, self.tilepos[0], self.tilepos[1]) #place a tile at each position
                        if bxst[1] < self.tilepos[1]:
                            self.fillBox(i, j, self.tilepos[0], bxst[1])
                    if bxst[0] < self.tilepos[0]:
                        if bxst[1] < self.tilepos[1]:
                            self.fillBox(i, j, bxst[0], bxst[1])
                        if bxst[1] > self.tilepos[1]:
                            self.fillBox(i, j, bxst[0], self.tilepos[1])
            self.parent.parent.tbox.boxstart = [] #clear the start position of the starting corner of selection box

    def fillBox(self, i, j, pos1, pos2): #this function creates one tile at a particular position within the selection box
        tm = self.parent.parent.tmap #easy reference to the entire tilemap array
        img = self.parent.parent.ibox.currentImage #easy reference to the current selected image
        path = self.parent.parent.ibox.currentImagePath #find the image location
        if tm.canvasarray [j + pos2] [i + pos1] != " ": # if a tile is already in the specified position
            self.delete(tm.canvasarray [j + pos2] [i + pos1]) #erase tile
        tm.canvasarray [j + pos2] [i + pos1] = ' ' #forget tile from canvas array
        tm.tilearray [j + pos2] [i + pos1] = ' ' #remove tile from tilemap
        #draw a tile at the specified position on the canvas
        canimg = self.create_image((i + pos1) * self.tsize, (j + pos2) * self.tsize, image=img, anchor = tk.NW)
        self.parent.parent.tmap.tilearray [j + pos2] [i + pos1] = path # put the tile in the tile array and canvas array
        self.parent.parent.tmap.canvasarray [j + pos2] [i + pos1] = canimg 
