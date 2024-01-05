from tkinter import *
from tkinter import colorchooser

def click():
    window.config(bg=colorchooser.askcolor()[1])
    # color = colorchooser.askcolor()
    # print(color)
    # coloHex = color[1]
    # print(coloHex)
    # window.config(bg=coloHex)


window = Tk()

window.geometry("420x420")

button = Button(window,text="Click Muiiii",
                command=click)
button.pack()


window.mainloop()