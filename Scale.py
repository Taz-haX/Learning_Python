from tkinter import *

def submit():
    print("The temparature is:", scale.get(), "Degrees C")

window = Tk()

coke = PhotoImage(file='boyo.png')
dok = PhotoImage(file='dogu.png')

cokes = Label(image=coke)
dokes = Label(image=dok)
cokes.pack()

scale = Scale(window,
              from_=100, to=0,
              length=600,
              orient=VERTICAL,
              font=("Impact", 18),
              tickinterval=10,
              #showvalue=0,
              #resolution=5,
              troughcolor="lime",
              fg="teal",
              bg="orange"
              )
scale.set((scale['from']-scale['to'])/2-scale['to'])
scale.pack()

dokes.pack()

button = Button(window, text="submit", command=submit)
button.pack()



window.mainloop()
