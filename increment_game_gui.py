from tkinter import *

# main window properties

main_window = Tk()
main_window.title("Increment Game")
main_window.geometry("800x800")
main_window.resizable(False, False) # non-resizable
main_window.configure(bg="lightblue")

# methods

def increase_score(): # increments score
    global score_value # accessible outside of function
    score_value += (increment * multiplier)
    score.configure(text="Your score: " + str(score_value))
    shop_score.configure(text="Your score: " + str(score_value))
    print("Score = " + str(score_value)) # debugging
    return score_value

def buy():
        multiplier *= 2
        
        return multiplier

def open_shop(): # shop window
    shop_window = Toplevel()
    shop_window.title("Shop")
    shop_window.geometry("500x500")
    shop_window.resizable(False, False)
    shop_window.configure(bg="lightyellow")
    global shop_score # must be global to update both windows
    shop_score = Label(shop_window, text= "Your score: " + str(score_value), font=("Courier", 15))
    shop_score.pack(side=TOP)
    global option1    
    option1 = Button(shop_window, text="Double click multiplier, Price: 50", font=("Courier", 10))
    option1.pack(side=BOTTOM)
    
    shop_window.mainloop()


# initial elements

score_value = 0
increment = 1
multiplier = 1

# main window elements

score = Label(main_window, text= "Your score: 0", font=("Courier", 20))
score.place(x=250,y=250)

increment_button = Button(main_window, text= "CLICK HERE", font=("Courier", 15), command=increase_score)
increment_button.place(x=250,y=300)

shop_button = Button(main_window, text= "SHOP", font=("Courier", 15), command=open_shop)
shop_button.place(x=250,y=350)

# window loop

mainloop()