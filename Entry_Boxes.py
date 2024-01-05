from tkinter import *


def submit():
    secretois = entry.get()
    print(secretois)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)


window = Tk()

entry = Entry(window,
              font=('Comic Sans', 50),
              fg="#73BA9B",
              bg="#D44D4D",
              show="$")

entry.insert(0, "Pajn")
entry.pack(side=LEFT)



submit_button = Button(window,
                       text="Submit",
                       command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="Delete",
                       command=delete)
delete_button.pack(side=RIGHT)

back_space_button = Button(window,
                       text="Backspace",
                       command=backspace)
back_space_button.pack(side=RIGHT)



window.mainloop()