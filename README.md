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
#### 1. Open Program
![Launch Program](https://github.com/Multilingual-Coder/Tile-Basic/blob/main/ReadmeImages/Step1.jpg)

To launch the Python script, run TileEditor.pyw. You will be greeted by the following screen.

![Opening Screen](https://github.com/Multilingual-Coder/Tile-Basic/blob/main/ReadmeImages/Step2.jpg)

The box on the top left is the image box. It will hold the images for tiles to be used in your game's tile map. To the right, you will see a dark grey box with scrollbars around it and a light grey grid overlayed on it. This is the canvas where you will place your tiles to form a tilemap. On the bottom left you will see a box with two icons in it. One looks like a cursor outline, and the other looks like an eraser outline. The cursor icon represents the "draw" tool, and the eraser icon represents the "eraser" tool. These tools will be used to edit your tile map visually on the canvas.

To get started go to the file menu and select "Open Image(s)" as shown below. If you are making a tilemap for a game, it is recommended that you first place all of your tile images in the directory you will be using for the images used in the game. This is because the tilemap editor will be remembering the images based on their path. So if you move one of the images later, the tilemap editor will not know how to find it.

![Opening Images](https://github.com/Multilingual-Coder/Tile-Basic/blob/main/ReadmeImages/Step3.jpg)

Once you select the "Open Image(s) option, an Open File Dialog will appear. Select all of the images that you want to use as tiles as shown in the image below. Then click "Open"


![Opening Images](https://github.com/Multilingual-Coder/Tile-Basic/blob/main/ReadmeImages/Step4.jpg)![Step1](https://user-images.githubusercontent.com/71729368/135165086-ab951f4e-6604-4965-ace4-b55e349ac1de.jpg)
![Step2](https://user-images.githubusercontent.com/71729368/135165089-338699a9-39fd-4985-a22f-14af40ae6b3b.jpg)
![Step3](https://user-images.githubusercontent.com/71729368/135165090-634a19c4-35b1-4268-add7-772a013e3803.jpg)
![Step4](https://user-images.githubusercontent.com/71729368/135165091-3306bc57-54bc-4db4-956b-47e9d2c2069f.jpg)
![Step5](https://user-images.githubusercontent.com/71729368/135165094-38b8f60c-8ad3-4474-a3f9-030203f85735.jpg)
![Step6](https://user-images.githubusercontent.com/71729368/135165098-0afbf8e5-dd7d-4b34-b537-ff615b626f52.jpg)
![Step7](https://user-images.githubusercontent.com/71729368/135165101-1e16dfc8-e10d-479d-900c-43f3aa5a7483.jpg)
![Step8](https://user-images.githubusercontent.com/71729368/135165102-ea2569a4-a6eb-42b9-92b4-d6151bce4192.jpg)
![Step9](https://user-images.githubusercontent.com/71729368/135165108-d1d02099-0602-437c-b00e-a0eb16dbe6d7.jpg)
![Step10](https://user-images.githubusercontent.com/71729368/135165110-477a8049-5830-4db3-af3a-65c1bdc0e5a4.jpg)
