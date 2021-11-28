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
import PIL.ImageTk
import PIL.Image
from tkinter import NW, messagebox

class Tile(): #class structure to hold images
    def __init__(self, path, size):
        self.size = size
        self.path = path
        self.image  = PIL.Image.open(open(path, 'rb')) #open a regular PIL image
        self.image = self.image.resize((self.size, self.size)) #resize the image to size we want tiles
        self.image = PIL.ImageTk.PhotoImage(self.image) #convert image to a tk displayable image

class TileMap():
    def __init__(self, parent, mapsize):
        self.mapsize = mapsize #sets the size of the map arrays
        self.parent = parent
        #create a tilemap matrix and a canvas object matrix of specified mapsize
        self.tilearray = []
        for i in range(self.mapsize):
            row =[]
            for j in range(self.mapsize):
                row.append(" ")      #fill them with spaces...
            self.tilearray.append(row)

        self.canvasarray = []
        for i in range(self.mapsize):
            row =[]
            for j in range(self.mapsize):
                row.append(" ")
            self.canvasarray.append(row)
    def OpenMap(self, path):
        try:
            file = open(path, "r") # open specified path...
            whole = file.read()
            file.close()
            data = whole.split("\n") # ...and split it into rows

            files = [] # make a holder for the paths to each tile image.
            for i,row in enumerate(data):
                if i > 6 and i < len(data) - 5 and row[13] == "i":
                    row = row[69:] # remove the "        self.images.append(pygame.transform.scale(pygame.image.load("...
                    row = row[:-36] #... and the "), (self.tilesize, self.tilesize)))" from the tile image path
                    files.append(str(row)) # append file to file types

            listdata = [] # make an intermediate array to hold the tilemap data
            begin = False
            for i, row in enumerate(data):
                if i > 6 and begin == False and row[13] == "a": # skip everything until array declaration.
                    begin = True
                if begin == True and i < len(data) - 5:# get everything until the drawMap() function definition
                    listdata.append(row)

            listdata[0] = listdata[0][23:] #remove the python array declaration
            array = [] #make a final holder for the tilemap data
            for row in listdata:
                item = row.replace("]", "").replace("[", "").replace(" ", "") # remove all unneeded chars
                item = item.split(",") #split array into pieces with newline char
                try: # if there is an empty "" left over...
                    item.remove("") # remove empty items left over from "]," at the end of each list
                except:
                    pass
                array.append(item) # add char to array

            self.NewFile() # clear the program data.

            self.parent.ibox.imgcanv.MakeButton(files) # make buttons for each loaded tile image.
            for i, row in enumerate(array):
                for j, elim in enumerate(row):
                    if(int(elim) > 0): # find each tile corresponding to an image
                        self.parent.ibox.imgcanv.selectTile(int(elim) - 1) 
                        self.parent.cframe.cmap.setTile((j, i)) # draw it to the screen
        except: # if there is an error loading file...
            # ask user if he/she would like to attempt to contiue anyway.
            mbox = messagebox.askyesno(title = "Loading Error", message = "There was an error loading file. The file has either been changed or is empty. Would you like to load it anyway?")
            if mbox == "no": # if not..
                self.NewFile() # clear the slate.

    def SaveMap(self, path, grabtype):
        pathtypes = [] # a list of all files that have already been detected during parsing
        pathtypes.append(" ") # add a default value so that spaces will always have the 0 or null value
        output  = "" # a list that holds the final file output
        filetype = ""
        count=0
        for char in str(path): # find the number of chars proceding the file extension...
            if char == "." or char == "{":
                break
            count+=1 # store it in count...
        for i in range(len(path) - count): 
            filetype += path[i + count] # ...and use it to find the path

        if filetype != ".py" and filetype != ".pyw" and filetype != ".csv": #set default file type to .py
            filetype = ".py" #if the user forgot to set his/her filetype when saving
            p2 = ""          #program automatically uses ".py" extension
            for i in range(count): #the path must be fixed to match what the user entered
                p2 += path[i]
            path = p2 + filetype
           
        arraydata = []
        if grabtype == "part": # if this save want to compress the map for a final export...
            truncate_row = True # this snippet will cut out all empty columns
            drop_rows_top = 0
            for row in self.tilearray: #finds the number of empty rows above map's contents
                for tile in row:
                    if tile != " ": # if row is not empty...
                        truncate_row = False # stop truncating rows.
                        break
                if truncate_row == False: # ...and break the loop
                    break
                drop_rows_top += 1 # update number of rows to drop on the top

            drop_rows_bottom = 0
            truncate_row_b = True
            for row in reversed(self.tilearray): #finds the number of empty rows below map's contents
                for tile in row:
                    if tile != " ": # if row is not empty...
                        truncate_row_b = False # stop truncating rows.
                        break
                if truncate_row_b == False: # ...and break the loop
                    break
                drop_rows_bottom += 1 # update number of rows to drop on the bottom
                
            drop_col_left = self.mapsize - 1
            for row in self.tilearray: #finds the number of empty columns left of map's contents
                col = 0
                for tile in row:
                    if tile != " ": # this method increments through each row and finds the column with the...
                        break #...tile that is closest to the left in that row. This value is then used to ...
                    else: #...find the left most column.
                        col += 1 # update the number of columns to drop
                if drop_col_left > col: # increment the number of columns to drop down from the total number of columns
                    drop_col_left = col

            drop_col_right = self.mapsize - 1
            for row in self.tilearray:
                col = 0
                for tile in reversed(row): #finds the number of empty columns right of map's contents
                    if tile != " ":# this method increments through each row and finds the column with the...
                        break #...tile that is closest to the right in that row. This value is then used to ...
                    else:#...find the right most column.
                        col += 1
                if drop_col_right > col:# increment the number of columns to drop down from the total number of columns
                    drop_col_right = col

            for x in range(drop_rows_top, self.mapsize - drop_rows_bottom): #cuts out all empty rows...
                row = []
                for y in range(drop_col_left, self.mapsize - drop_col_right):
                    row.append(self.tilearray[x][y])#...leaving only the map contents
                arraydata.append(row)
        else:
            arraydata = self.tilearray #if the user does not want to compress output, use the entire map.

        for row in arraydata:
            for tile in row:
                found = False
                count = 0
                for p in pathtypes: #finds each image path and assigns it a number...
                    if tile == p:
                        found = True
                        break
                    else:
                        count += 1
                if found == False:
                    pathtypes.append(tile)
                output += str(count) + "," #...the numbers are added to the output
            output += "\n"
        try: #use error handling in case file cannot be written to.
            if filetype == ".csv": # if the user's selected filetype is .csv...
                file = open(path, "w") #just dump the array data in the file
                file.write(output)
                file.close()
            if filetype == ".py" or filetype == ".pyw": # This code writes a python file that loads and draws a map using pygame.
                output2 = '''import pygame

class TileMap():
    def __init__(self, tilesize):
        pygame.init()
        self.tilesize = tilesize
        self.images = []\n'''

                for i in range(len(pathtypes)): # write a line of code that loads a tile image...
                    if i > 0: #for each tile that the user loaded.
                        output2 += '''        self.images.append(pygame.transform.scale(pygame.image.load("''' + str(pathtypes[i]) + '''"), (self.tilesize, self.tilesize)))\n'''

                data = output.split("\n") #split the output string by the new line character splitting it into an array.
                output2 += "        self.array = ["
                for i in range(len(data) - 1): # write code to load the tile array.
                    if i != 0: output += "        "
                    output2 += "[" + data[i][:-1] + "],\n"
                output2 = output2[:-2] + "]\n"
                # make a function to draw all of the tiles to the screen
                output2 += '''    def drawMap(self, surface, location):
            for i,row in enumerate(self.array):
                for j,tile in enumerate(row):
                    if tile > 0:
                        surface.blit(self.images[tile - 1], (location[0] + j * self.tilesize, location[1] + i * self.tilesize))'''

                file = open(path, "w") #output goes to file
                file.write(output2)
                file.close()
        except:
           messagebox.showwarning(message="File " + str(path) + " cannot be written to. Make sure it is not open in another program and then try again.")

    def NewFile(self): # a function that clears the screen and array data.
        for i, row in enumerate(self.canvasarray):
            for j, tile in enumerate(row):
                self.parent.cframe.cmap.delete(tile) # delete all tiles on the screen.
                self.canvasarray[i][j] = ' ' # clear the canvas array
        for i, row in enumerate(self.tilearray):
            for j,tile in enumerate(row):
                self.tilearray[i][j] = ' ' # clear the tile array.
        self.parent.ibox.imgcanv.buttons.clear() # clear all tile buttons in the side box.
        for item in self.parent.ibox.imgcanv.winfo_children():
            item.destroy()

            self.parent.ibox.imgcanv.newbtnpos = (0, 0) # Set the starting position for button placement so original position
