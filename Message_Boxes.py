from tkinter import *

from tkinter import messagebox

def click():
    answer = messagebox.askyesnocancel(title="y/n/c",message="you like livin?")
    if answer==True:
        print("sadge")
    elif answer==False:
        print("Us nakeee")
    else:
        print("ANSWER THE QUESTIONNN")
    # answer = messagebox.askquestion(title="Question",message="You ded?")
    # if answer == "yes":
    #     print("no you not boi")
    # else:
    #     print("how you sure?")
    # if messagebox.askyesno(title="Yey or Ney?", message="like being an idiot?"):
    #     print("weirdo")
    # else:
    #     print("exactly what an idiot would say")
    # if messagebox.askretrycancel(title="Ask,ok,cancel", message="whatcha want"):
    #     print("mummy, i did a thing")
    # else:
    #     print("oh look, incompetent")
    # if messagebox.askokcancel(title="Ask,ok,cancel", message="whatcha want"):
    #     print("mummy, i did a thing")
    # else:
    #     print("oh look, incompetent")
    #messagebox.showerror(title="Warning", message="lol put")
    #while True:
        #messagebox.showwarning(title="Warning", message="lol put")

    #messagebox.showinfo(title="Warning", message="Why you sad boi?")


window =Tk()

button = Button(window,
                command=click, text="Click me boyo"
                )
button.pack()

window.mainloop()