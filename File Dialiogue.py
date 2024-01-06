
from tkinter import *
from tkinter import filedialog
def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\HP\\Downloads",
                                          title="Open Files",
                                          filetypes=(("Text files","*.txt"),("All files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(window,
                text="Open",
                command=openFile)
button.pack()

window.mainloop()