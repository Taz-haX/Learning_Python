from tkinter import *

window = Tk()

frame = Frame(window, bg='blue',bd='5',relief=SUNKEN)
#frame.pack(side=BOTTOM)
frame.place(x=10,y=10)

Button(frame,text='W',font=('Consolas',20),width=3).pack(side=TOP)
Button(frame,text='A',font=('Consolas',20),width=3).pack(side=LEFT)
Button(frame,text='S',font=('Consolas',20),width=3).pack(side=LEFT)
Button(frame,text='D',font=('Consolas',20),width=3).pack(side=LEFT)
window.mainloop()