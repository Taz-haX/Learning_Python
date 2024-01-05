from tkinter import *

def submit():
    into = text.get("1.0",END)
    print(into)


window = Tk()

text = Text(window,
            bg="Light Yellow",
            font=("Ink Free",18),
            height=10,
            width=25,
            padx=5,
            pady=5,
            fg="Teal")
text.pack()

button = Button(window, text="Submit", command=submit)
button.pack()


window.mainloop()