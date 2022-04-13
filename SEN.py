from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk


myWidth = 1080
myHeight = 720

root = Tk()
root.geometry(f"{myWidth}x{myHeight}")
root.title("RJ-PhotoShope")
root.iconbitmap("logo.ico")
root.config(bg='#222')

##### Added menuBar #####
menuBar = Menu(root)

##### Added canvas #####
canva = Canvas(root, width=myWidth-20, height=myHeight-20, bg='#ccc').pack(pady=40)
canva.create_image(10, 10, anchor=NW, image=PhotoImage('D://SY_Projects//logo.png'))

img = None

def openImg():
    global img
    global canva
    imgPath = askopenfilename(defaultextension=".png", filetypes=[("png", "*.png"),
                                                                ("jpg", "*.jpg"),
                                                                ("jpeg", "*.jpeg"),
                                                                ("All files", "*.*"), ])
    img = Image.open(imgPath)
    photo = ImageTk.PhotoImage(img)
    canva.create_image(10, 10, anchor=NW, image=photo)
    root.update()
    print(imgPath)


def saveImg():
    imgPath = asksaveasfilename(initialfile="Untitled.png", defaultextension=".png", filetypes=[("png", "*.png"),
                                                                                                ("All files", "*.*"),
                                                                                                ("jpg", "*.jpg"),
                                                                                                ("jpeg", "*.jpeg"), ])
    print(imgPath)


def refresh():
    root.update()


def rotate90Clockwise():
    global imgObj, photo
    print(imgObj)
    imgObj =imgObj.rotate(-90)
    
    imgObj.show()


def rotate90AntiClockwise():
    pass


def rotateCustom():
    pass


def resizeImg():
    pass


def reflectImg():
    pass


def cropImg():
    pass

##### Added fileMenu #####
fileMenu = Menu(root, tearoff=0, font=("Times", 12))
fileMenu.add_command(label="Open", command=openImg)
fileMenu.add_command(label="Save", command=saveImg)
fileMenu.add_separator()
fileMenu.add_command(label="Refresh", command=refresh)
fileMenu.add_command(label="Exit", command=quit)
menuBar.add_cascade(label="File", menu=fileMenu)

##### Added EditMenu #####
editMenu = Menu(root, tearoff=0, font=("Times", 12))
editMenu.add_command(label="Rotate 90", command=rotate90Clockwise)
editMenu.add_command(label="Rotate 90", command=rotate90AntiClockwise)
editMenu.add_command(label="Rotate", command=rotateCustom)
editMenu.add_separator()
editMenu.add_command(label="Resize", command=resizeImg)
editMenu.add_command(label="Reflect", command=reflectImg)
editMenu.add_command(label="Crop", command=cropImg)
menuBar.add_cascade(label="Edit", menu=editMenu)

root.config(menu=menuBar)

root.mainloop()
