from tkinter import *

def click():
    print("Now you happpy")

window = Tk()    #instantiate an instacne of a window



window.geometry("420x420")
window.title("HAhA boi")

iconic = PhotoImage(file='received_374634148166240.png')
window.iconphoto(True,iconic)

window.config(background="teal")

photo = PhotoImage(file="png-transparent-pink-cross-stroke-ink-brush-pen-red-ink-brush-ink-leave-the-material-text-thumbnail.png")

label = Label(window,
              text="Life be sad",
              font=('Arial',40,'bold'),
              fg='orange',
              bg='teal',
              relief=RAISED,
              bd=5,
              padx=100,
              image=photo,
              compound='bottom')




label.pack()
#label.place(x=100,y=50)


window.mainloop()