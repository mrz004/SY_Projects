from tkinter import *
from tkinter import Canvas
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageOps

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
canvas = Canvas(root, width=myWidth - 20, height=myHeight - 20, bg='#ccc')
canvas.pack(pady=40)
imgRef = PhotoImage(file="D:\SY_Projects\logo.png")
# canvas.create_image(10, 10, anchor=NW, image=imgRef)

img = None


def openImg(imgpath=True):
    global img
    global imgRef
    if imgpath:
        imgPath = askopenfilename(defaultextension=".png", filetypes=[("png", "*.png"),
                                                                      ("jpg", "*.jpg"),
                                                                      ("jpeg", "*.jpeg"),
                                                                      ("All files", "*.*"), ])
        img = Image.open(imgPath)
        print(imgPath)
    imgRef = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, anchor=NW, image=imgRef)
    root.update()


def saveImg():
    imgPath = asksaveasfilename(initialfile="Untitled.png", defaultextension=".png", filetypes=[("png", "*.png"),
                                                                                                ("All files", "*.*"),
                                                                                                ("jpg", "*.jpg"),
                                                                                                ("jpeg", "*.jpeg"), ])
    print(imgPath)


def refresh():
    root.update()


def rotate90Clockwise():
    global img
    # print(img)
    img = img.rotate(-90, expand=True)
    openImg(imgpath=False)


def rotate90AntiClockwise():
    global img
    img = img.rotate(90, expand=True)
    openImg(imgpath=False)


def rotateCustom():

    def apply():
        global img
        # print(rotationAngle.get())
        img = img.rotate(int(rotationAngle.get())*-1, expand=True)
        openImg(imgpath=False)
        rotatBox.destroy()

    rotatBox = Tk()
    msg = Label(rotatBox, text="Enter rotation angle").pack(padx=20, pady=10)
    rotationAngle = Entry(rotatBox)
    rotationAngle.pack(padx=20, pady=10)
    submit = Button(rotatBox, text="Apply", command=apply).pack(padx=20, pady=5)
    rotatBox.mainloop()


def resizeImg():
    pass


def reflectImgVertical():
    global img
    img = ImageOps.flip(img)
    openImg(imgpath=False)


def reflectImgHorizontal():
    global img
    img = ImageOps.mirror(img)
    openImg(imgpath=False)


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
editMenu.add_command(label="Rotate Clockwise 90", command=rotate90Clockwise)
editMenu.add_command(label="Rotate Anti-Clockwise 90", command=rotate90AntiClockwise)
editMenu.add_command(label="Rotate", command=rotateCustom)
editMenu.add_separator()
editMenu.add_command(label="Resize", command=resizeImg)
editMenu.add_command(label="Reflect Vertically", command=reflectImgVertical)
editMenu.add_command(label="Reflect Horizontally", command=reflectImgHorizontal)
editMenu.add_command(label="Crop", command=cropImg)
menuBar.add_cascade(label="Edit", menu=editMenu)

root.config(menu=menuBar)

root.mainloop()
