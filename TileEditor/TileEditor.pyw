 #   This file is part of Tile Basic. This is the main entry point for  the Tile Basic Tile Editor
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
from tkinter import messagebox
from mods import *

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self) #Inherits the main window from tkinnter
        self.saved = True #holds a value for whether or not  the tilemap has been saved
        self.title("Tile Basic")
        self.tmap = TileMap(self, 125) #creates an object that holds the images, canvas objects, and paths for our tilemap
        self.ibox = ImageFrame(self) #creates the box that holds our tiles
        self.tbox = ToolFrame(self) #creates a box that holds our tools
        self.tbar = TopBar(self) #creates the window's topbar
        self.cframe = CanvasFrame(self)
        self.protocol("WM_DELETE_WINDOW", self.Quit) #changes what the window does when we click to close it
        self.mainloop()

    def Quit(self):
        if self.saved:
            self.destroy() #destroy the window if everything is saved...
        else: #...otherwise, ask the user if he/she wants to save his/her work
            mbox = tk.messagebox.askquestion(title="Save File", 
                                             message="Some changes are unsaved! Would you like to save your progress?")
            if mbox=="no": #if no, end the program without saving
                self.destroy()
            else:
                self.tbar.fmenu.SaveProgress() #otherwise, save.

app = MainApp()
