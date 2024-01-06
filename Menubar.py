from tkinter import *

def openn():
    print("Okay opened")
def savu():
    print("ya savin'")
def cutti():
    print("Malevolent Kitchen")
def pastr():
    print("Copy Pasting")
def cope():
    print("Takin copium")
window = Tk()

saveIm = PhotoImage(file='savant.png')
opIm = PhotoImage(file='lifeant.png')
exIm = PhotoImage(file='escapant.png')

menubar = Menu(window)
window.geometry("300x300")
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=('Times New Roman',10))
menubar.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="Open",command=openn,image=opIm,compound=LEFT)
fileMenu.add_command(label="Save",command=savu,image=saveIm,compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exIm,compound=LEFT)

editMenu = Menu(menubar,tearoff=0,font=('Arial',8))
menubar.add_cascade(label="Edit",menu=editMenu)

editMenu.add_command(label="Cut",command=cutti)
editMenu.add_command(label="Paste",command=pastr)
editMenu.add_separator()
editMenu.add_command(label="Copy",command=cope)

window.mainloop()