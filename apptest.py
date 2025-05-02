from tkinter import *


    
window = Tk()
window.title("Test")
window.geometry("500x500")

lbl = Label(window, text="Password length: ") # label
lbl.grid()

txt = Entry(window, width=10)
txt.grid(column=1, row=0)

def click():
    typed_text = "You typed: " + txt.get()
    lbl.configure(text = typed_text)

button = Button(window, text="Click here", fg="green", command=click)
button.grid(column=2,row=0)

window.mainloop()