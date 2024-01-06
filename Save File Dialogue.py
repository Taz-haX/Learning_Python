from tkinter import *
from tkinter import filedialog
def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\HP\\Downloads",
                                    defaultextension=".txt",
                                    filetypes=[("Text file","*.txt"),
                                               ("html files","*.html"),
                                               ("All files","*.*")])
    if file is None:
        return
    filetxt = str(text.get("1.0",END))
    file.write(filetxt)
    file.close()


window = Tk()

button = Button(window,text="save",command=saveFile)
button.pack()
text = Text(window)
text.pack()





window.mainloop()