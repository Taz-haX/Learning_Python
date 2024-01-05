from tkinter import *

def add():
    listbox.insert(listbox.size(),entry_box.get())
    listbox.config(height=listbox.size())

def submit():
    #y = listbox.get(listbox.curselection())
    orders = []

    for index in listbox.curselection():
        orders.insert(index,listbox.get(index))
    print("You have ordered: ", end="")
    print()
    for index in orders:

        print(index)

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg="teal",
                  font=('Arial', 40),
                  width=10,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Hamburger")
listbox.insert(3, "Shakes")
listbox.insert(4, "Coffee")
listbox.insert(5, "Fries")

listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

add_button = Button(window,
                       text="Add",
                       command=add)
add_button.pack()

delete_button = Button(window,
                       text="Delete",
                       command=delete)
delete_button.pack()

submit_button = Button(window,
                       text="Order",
                       command=submit)
submit_button.pack()


window.mainloop()
