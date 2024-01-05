from tkinter import *

def display():
    if (x.get()==1):
        print("Ye agree bose")
    else:
        print("Why dontcha agree boi")


window = Tk()

howe = PhotoImage('received_374634148166240.png')

x = IntVar()

dowe = PhotoImage(file='png-transparent-pink-cross-stroke-ink-brush-pen-red-ink-brush-ink-leave-the-material-text-thumbnail.png')

check_button = Checkbutton(window,
                           text="Hehe OK",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           fg="green",
                           bg="yellow",
                           activebackground="yellow",
                           activeforeground="green",
                           padx=50,
                           image=dowe,
                           compound=LEFT)

check_button.pack()



window.mainloop()
