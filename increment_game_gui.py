from tkinter import *
from time import strftime

# main window properties

main_window = Tk()
main_window.title("Increment Game")
main_window.geometry("800x800")
main_window.resizable(False, False) # non-resizable
main_window.configure(bg="lightblue")

# shop window properties

shop_window = Toplevel()
shop_window.title("Shop")
shop_window.geometry("500x500")
shop_window.resizable(False, False)
shop_window.configure(bg="lightyellow")
shop_window.withdraw() # shop window is initially hidden
shop_window.protocol("WM_DELETE_WINDOW", shop_window.withdraw) # overrides default "close" button action with withdrawal

# methods

def time(): # timer display function
    time_value = strftime("%H:%M:%S %p")
    time_label.configure(text=time_value)
    time_label.after(1000, time)

def increase_score(): # increments score
    global score_value # accessible outside of function
    score_value += (increment * multiplier)
    score.configure(text="Your score: " + str(score_value))
    shop_score.configure(text="Your score: " + str(score_value))
    print("Score = " + str(score_value)) # debugging
    return score_value

def buy(price, effect, button, alert):
        global score_value
        if score_value >= price:
            score_value -= price
            effect()
            if button:
                button.pack_forget()
            score.configure(text="Your score: " + str(score_value))
            shop_score.configure(text="Your score: " + str(score_value))
            if alert:
                alert.pack_forget()
        else:
            if alert:
                alert.configure(text="Not enough score.")
                alert.pack(side=TOP)

def open_shop(): # shop window
    shop_window.deiconify() # shows shop window, initially hidden

# purchase effects

def multiplier_increase(mi):
    global multiplier
    multiplier *= mi

def increment_increase(ii):
    global increment
    increment += ii

def auto_click(frequency):
    def ac():
        increase_score()
        main_window.after(frequency, ac)
    ac()

# initial elements

score_value = 0
increment = 1 # gain 1 score initially for pressing button
multiplier = 1 # x1 multiplier for increment initially

# main window elements

time_label = Label(main_window, font=("Courier", 15, "bold"))
time_label.place(x=100, y=50)

score = Label(main_window, text= "Your score: 0", font=("Courier", 20))
score.place(x=250,y=250)

increment_button = Button(main_window, text= "CLICK HERE", font=("Courier", 15), command=increase_score)
increment_button.place(x=250,y=300)

shop_button = Button(main_window, text= "SHOP", font=("Courier", 15), command=open_shop)
shop_button.place(x=250,y=350)

# shop window elements

global shop_score # must be global to update both windows
shop_score = Label(shop_window, text= "Your score: " + str(score_value), font=("Courier", 15))
shop_score.pack(side=TOP)
alert = Label(shop_window, text= "", font=("Courier", 15), fg="red") # initially not shown
global option1
option1 = Button(shop_window, text="Double click multiplier, Price: 50", font=("Courier", 10), command=lambda: buy(50, lambda: multiplier_increase(2), option1, alert)) # lambda delays effect until prerequisite is met
option1.pack(side=BOTTOM)

# window loop and additional function calls

time()
mainloop()