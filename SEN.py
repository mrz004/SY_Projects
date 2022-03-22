from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk


whidth = 1080
hight = 720

root = Tk()
root.geometry(f"{whidth}x{hight}")
root.title("RJ-PhotoShope")
root.iconbitmap("logo.ico")
root.config(bg='#222')


img = Label(root)
imgNotSet = True
photo = None
imgObj = None

def openImg(openfileDilog=True):
    global img
    global imgObj
    global imgNotSet
    global photo
    if openfileDilog:
        imgPath = askopenfilename(defaultextension=".png", filetypes=[("png", "*.png"),
                                                                    ("jpg", "*.jpg"),
                                                                    ("jpeg", "*.jpeg"),
                                                                    ("All files", "*.*"), ])
        imgObj = Image.open(imgPath)
        photo = ImageTk.PhotoImage(imgObj)
    if imgNotSet:
        img = Label(midPart, image=photo).pack()
        imgNotSet = False
    else:
        img.pack_forget()
        img = Label(midPart, image=photo).pack()
    # img = photo
    photo = photo
    root.update()
    print(imgPath)
    print(imgNotSet)


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
    photo = ImageTk.PhotoImage(imgObj)
    photo = photo
    
    root.update()
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


#############################################    Top part    #############################################
topPart = Frame(root).pack(anchor=N, side=TOP)

##### Added menuBar #####
menuBar = Menu(root)

##### Added fileMenu #####
fileMenu = Menu(menuBar, tearoff=0, font=("Times", 12))
fileMenu.add_command(label="Open", command=openImg)
fileMenu.add_command(label="Save", command=saveImg)
fileMenu.add_separator()
fileMenu.add_command(label="Refresh", command=refresh)
fileMenu.add_command(label="Exit", command=quit)
menuBar.add_cascade(label="File", menu=fileMenu)

##### Added EditMenu #####
editMenu = Menu(menuBar, tearoff=0, font=("Times", 12))
editMenu.add_command(label="Rotate 90", command=rotate90Clockwise)
editMenu.add_command(label="Rotate 90", command=rotate90AntiClockwise)
editMenu.add_command(label="Rotate", command=rotateCustom)
editMenu.add_separator()
editMenu.add_command(label="Resize", command=resizeImg)
editMenu.add_command(label="Reflect", command=reflectImg)
editMenu.add_command(label="Crop", command=cropImg)
menuBar.add_cascade(label="Edit", menu=editMenu)

root.config(menu=menuBar)

#############################################    Side left    #############################################
sideLeft = Frame(root, padx=5, pady=0).pack(anchor=W, side=LEFT)

#############################################    Middel part    #############################################
midPart = Frame(root, padx=5, pady=0).pack(anchor=W, side=RIGHT)

#############################################    Side right    #############################################
sideRight = Frame(root, padx=5, pady=0).pack(anchor=E, side=RIGHT)

root.mainloop()
