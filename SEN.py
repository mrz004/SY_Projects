from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk

def openImg():
    imgPath = askopenfilename(defaultextension=".png", filetypes=[("png", "*.png"),
                                                                    ("All files", "*.*"),
                                                                    ("jpg", "*.jpg"),
                                                                    ("jpeg", "*.jpeg"),])
    if imgPath != None:
        photo = ImageTk.PhotoImage(Image.open(imgPath))
        img = Label(midPart, image=photo).pack()
        img.image = photo
        root.update()
        print(imgPath)

def saveImg():
    imgPath = asksaveasfilename(initialfile="Untitled.png", defaultextension=".png", filetypes=[("png", "*.png"),
                                                                                                                                                        ("All files", "*.*"),
                                                                                                                                                        ("jpg", "*.jpg"),
                                                                                                                                                        ("jpeg", "*.jpeg"),])
    print(imgPath)

def refresh():
    root.update()

def rotate90Clockwise():
    pass

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

whidth = 1080
hight = 720

if __name__ == '__main__':

    root = Tk()
    root.geometry(f"{whidth}x{hight}")
    root.title("RJ-PhotoShope")
    root.iconbitmap("logo.ico")
    root.config(bg='#222')

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