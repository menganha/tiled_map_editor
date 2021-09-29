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
import tkinter as tk

class TopBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent) #inherits from menu class making a menu
        self.parent = parent #holds access the parent (main window)
        self.parent.config(menu=self) #configurt the main window with a top bar
        self.fmenu = FileMenu(self) #create a FileMenu object which will make a file menu dropdown

class FileMenu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent, tearoff=0)
        self.parent = parent #holds access to parent (Top Bar)
        self.add_command(label="New", command = self.FileNew) #make this clear canvas next........
        self.add_command(label="Open Map", command = self.OpenMap)
        self.add_command(label="Save Map", command = self.SaveProgress)
        self.add_command(label="Open Image(s)", command = parent.parent.ibox.OpenImage)
        self.add_command(label="Quit", command=self.parent.parent.Quit) #calls for the parent's parent (main window)
                                                                        #to run the Quit function
        self.parent.add_cascade(label = "File", menu=self) #add file menu cascade to the file menu option

    def SaveProgress(self):
        option = tk.IntVar() # create a holder for the save options
        self.dialog = tk.Toplevel(self.parent.parent) # create a dialog to hold the radio buttons
        self.dialog.title("Choose Save Method")
        rb1 = tk.Radiobutton(self.dialog, text = "Save only section of map containing tiles (better for using in a game)", variable = option, value = 1)
        rb1.pack(anchor = tk.W) # add a radio button to dialog box for option 1
        rb1.select()
        rb2 = tk.Radiobutton(self.dialog, text = "Save whole tile map with empty sections (better for an intermediate save)", variable = option, value = 2)
        rb2.pack(anchor = tk.W) # add a radio button to dialog box for option 2
        btn = tk.Button(self.dialog, text = "Ok", width = 5, command = lambda i = option: self.Save(i))
        btn.pack() # add a button the user can click when the user has made his/her decision

    def Save(self, var):
        self.dialog.destroy() #close the dialog window
        self.parent.parent.saved = True # let program know that the user has saved progress.
        if var.get() ==  1: # get the user's chosen save method
            c = "part"
        else:
            c = "whole"
        
        # make a dialog box with which the user can choose a save location.
        fts  = [("Python File", ".py .pyw"), ("Comma Seperated", ".csv")]
        path = tk.filedialog.asksaveasfilename(title="Save Tile Map",
                                           filetypes = fts, defaultextension = fts)
        self.parent.parent.tmap.SaveMap(path, c) # save the map to specified file.

    def OpenMap(self):
        path = '' # make a dialog box with which the user can specify a file to open.
        path = tk.filedialog.askopenfilename(title = "Open Map", filetypes = [("Python Files", ".py .pyw")])
        if path != '':
            self.parent.parent.tmap.OpenMap(str(path)) # open specified path.

    def FileNew(self):
        if self.parent.parent.saved == False: # if the program has not been saved...
            mbox = tk.messagebox(title = "Save File", # allow the user to specify if he/she would like to save progress first.
                               message="Some changes are unsaved! Would you like to save your progress?")
            if mbox == "no": # if not...
                self.parent.parent.tmap.NewFile() # make new file
            else: # if the user does want to save first
                self.SaveProgress() #...save file
                saved = True
        else: # if the program has been saved...
            self.parent.parent.tmap.NewFile() # clear program data 
