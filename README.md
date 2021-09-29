# Tile-Basic v0.1
This is a simple tile editor for pygame game developers. This program allows the user to visually create a tilemap that can then be exported as pygame code. The resulting code will create pygame code that will load the tilemap and draw it to the pygame screen.

### Dependencies
#### Tkinter
Tkinter provides the program with a graphical user interface. To run this script, you will need the Tkinter library installed. 

Windows and MacOS:
  If you are using Windows or MacOS you should already have tkinter built in your python distribution.

Linux:
  If you are using a debian based linux distribution and you do not already have tkinter installed, run the command
  ```
  sudo apt-get install python3-tk
  ```
#### Pillow
Pillow provides the program with a quick and easy way to load, draw, and manipulate images. To run this python script, you will need the Pillow imaging library. To install the Pillow, run the following commands:

```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
Once Pillow and Tkinter are installed, you should be ready to run the program.

### How To Use
#### 1. Opening Program
![Launch Program](https://user-images.githubusercontent.com/71729368/135165553-6b96e732-dc10-4fcc-a8f0-abb564947682.jpg)

To launch the Python script, run TileEditor.pyw. You will be greeted by the following screen.

![Opening Screen](https://user-images.githubusercontent.com/71729368/135165738-bd5fa826-2ee9-4518-9bf0-2fc0a2411eb9.jpg)



The box on the top left is the image box. It will hold the images for tiles to be used in your game's tile map. To the right, you will see a dark grey box with scrollbars around it and a light grey grid overlayed on it. This is the canvas where you will place your tiles to form a tilemap. On the bottom left you will see a box with two icons in it. One looks like a cursor outline, and the other looks like an eraser outline. The cursor icon represents the "draw" tool, and the eraser icon represents the "eraser" tool. These tools will be used to edit your tile map visually on the canvas.

#### 2. Opening Tile Images
To get started go to the file menu and select "Open Image(s)" as shown below. If you are making a tilemap for a game, it is recommended that you first place all of your tile images in the directory you will be using for the images used in the game. This is because the tilemap editor will be remembering the images based on their path. So if you move one of the images later, the tilemap editor will not know how to find it.

![Opening Images](https://user-images.githubusercontent.com/71729368/135165963-43be5d2f-38ad-4eb2-bc32-076cc84c6d8c.jpg)

Once you select the "Open Image(s)" option, an Open File Dialog will appear. Select all of the images that you want to use as tiles as shown in the image below. Then click "Open".


![Opening Images](https://user-images.githubusercontent.com/71729368/135165091-3306bc57-54bc-4db4-956b-47e9d2c2069f.jpg)

The Selected images will be loaded into the image box as shown below. Click one of the tile icons to select it.

![Image Box](https://user-images.githubusercontent.com/71729368/135165094-38b8f60c-8ad3-4474-a3f9-030203f85735.jpg)

#### 3. Tools and Map Editing

Draw the tiles onto the Canvas as desired. Click and drag to draw multiple tiles. You are currently using the "draw" tool. 

![Draw Map](https://user-images.githubusercontent.com/71729368/135165098-0afbf8e5-dd7d-4b34-b537-ff615b626f52.jpg)

If you would like to erase any part of your tile map, select the eraser tool by clicking on it. Then click on the tile that you would like to erase. Click and drag to erase multiple tiles. You are currently using the "eraser" tool. If you would like to switch back to the "draw" tool to add more tiles to your map, click a tile icon in the image box, or click the "draw tool icon.

![Eraser Tool](https://user-images.githubusercontent.com/71729368/135165101-1e16dfc8-e10d-479d-900c-43f3aa5a7483.jpg)

#### 4. Saving Your Map

Once you are done editing your tilemap, go to the file menu and click "Save Map".

![Save Map](https://user-images.githubusercontent.com/71729368/135165108-d1d02099-0602-437c-b00e-a0eb16dbe6d7.jpg)

You will be confronted with a dialog box like the one shown below. It will ask you if you want to save only the section of your map containing tiles or if you would like to save the entire map (including empty rows). If you are going to use your tile map in your game immediately, it might be best to save the map without any empty rows as these might get in your way when you try to draw the map to your screen in your game. If, however, you want to save your map for later editing before you use it in your game, it is best to save the entire map with the empty rows.

![Save Type Dialog](https://user-images.githubusercontent.com/71729368/135165110-477a8049-5830-4db3-af3a-65c1bdc0e5a4.jpg)

Choose a save location and name and click "Save".

![Save File](https://user-images.githubusercontent.com/71729368/135165556-f7b99457-6eca-4083-863a-6f78e71be562.jpg)

#### 5. Using Your Tile Map Code



#### 6. Open Previous Project

If you would like to reopen a previously saved project, go to the file menu and click "Open Map".

![Open Map](https://user-images.githubusercontent.com/71729368/135165562-66deae26-fc43-4c1d-b234-e24953b16e2b.jpg)

Navigate to the location of the saved file and open it.

![Open Map](https://user-images.githubusercontent.com/71729368/135165566-f3067213-16ba-46f1-8b6f-7c002cec0a8d.jpg)

Your tile map will be loaded into the tile editor. You can now edit it and save it again with the new changes.

![Loaded File](https://user-images.githubusercontent.com/71729368/135165569-6e3bda35-caaa-4134-90ae-4e6d70a8a955.jpg)
