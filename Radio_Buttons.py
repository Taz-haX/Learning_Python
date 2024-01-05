from tkinter import *

food = ["Hamburger","Pizza","Donuts"]

def order():
    if(x.get()==0):
        print("Ew hamburger")
    elif(x.get()==1):
        print("Pizza yeyyy")
    elif(x.get()==2):
        print("Donut? Seriously?")
    else:
        print("what? W H A T ?")

window = Tk()

ham_pic = PhotoImage(file="hambu.png")
piz_pic = PhotoImage(file="pija.png")
do_pic = PhotoImage(file="donu.png")

food_image = [ham_pic, piz_pic, do_pic]

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value=index,
                               padx=25,
                               font=("Arial",30),
                               indicatoron=0, #image=food_image[index],
                               width=20,
                               command=order
                               )
    radio_button.pack(anchor=W)


window.mainloop()