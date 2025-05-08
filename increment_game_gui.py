from tkinter import *
from time import strftime
import json # for saves

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
shop_window.configure(bg="gold")
shop_window.withdraw() # shop window is initially hidden
shop_window.protocol("WM_DELETE_WINDOW", shop_window.withdraw) # overrides default "close" button action with withdrawal

# save window properties

save_window = Toplevel()
save_window.title("Save")
save_window.geometry("500x200")
save_window.resizable(False,False)
save_window.configure(bg="aquamarine")
save_window.withdraw()
save_window.protocol("WM_DELETE_WINDOW", save_window.withdraw)

# load window properties

load_window = Toplevel()
load_window.title("Load")
load_window.geometry("500x200")
load_window.resizable(False,False)
load_window.configure(bg="aquamarine")
load_window.withdraw()
load_window.protocol("WM_DELETE_WINDOW", load_window.withdraw)

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

def ac_increase_score(): # unique function for autoclick score
    global score_value
    score_value += (auto_click_increment * auto_click_multiplier)
    score.configure(text="Your score: " + str(score_value))
    shop_score.configure(text="Your score: " + str(score_value))
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
            score_per_click.configure(text="Score gain per click: " + str(increment * multiplier))
            ac_score_per_click.configure(text="Auto click score gain per click: " + str(auto_click_increment * auto_click_multiplier))
            
            if alert:
                alert.pack_forget()
        else:
            if alert:
                alert.configure(text="Not enough score.")
                alert.pack(side=TOP)
                alert.after(5000, lambda: alert.destroy()) # destroy message after 5 seconds


def open_shop(): # shop window
    shop_window.deiconify() # shows shop window, initially hidden

def open_saves(): # save window
    save_window.deiconify()

def open_loads(): # load window
    load_window.deiconify()

def save_file(file, save_alert): # save current data to json
    data = {
        "score_value":score_value,
        "increment":increment,
        "multiplier":multiplier,
        "ac_increment": auto_click_increment,
        "ac_multiplier": auto_click_multiplier
        
    }
    path = str(file) + ".json"
    with open(path, 'w') as save_data:
        json.dump(data, save_data, indent=4)
    if save_alert:
        save_alert.configure(text=f"Game data has been saved to {path}.")
        save_alert.pack(side=TOP)
        print(f"Game data has been saved to {path}.")
        save_alert.after(5000, lambda: save_alert.destroy())
    

# purchase effects

def multiplier_increase(mi):
    global multiplier
    multiplier *= mi

def increment_increase(ii):
    global increment
    increment += ii

def ac_multiplier_increase(ami):
    global auto_click_multiplier
    auto_click_increment *= ami
    
def ac_increment_increase(aii):
    global auto_click_increment
    auto_click_increment += aii

def auto_click(frequency, aii):
    ac_increment_increase(aii)
    def ac():
        ac_increase_score()
        main_window.after(frequency, ac) # recursive call
    ac()

# initial elements

score_value = 0
increment = 1 # gain 1 score initially for pressing button
multiplier = 1 # x1 multiplier for increment initially
auto_click_increment = 0
auto_click_multiplier = 1

# main window elements

time_label = Label(main_window, font=("Courier", 15, "bold"))
time_label.place(x=100, y=50)

score_per_click = Label(main_window, text= "Score gain per click: " + str(increment * multiplier), font=("Courier", 20))
score_per_click.place(x=100,y=100)
score = Label(main_window, text= "Your score: 0", font=("Courier", 20))
score.place(x=250,y=250)

ac_score_per_click = Label(main_window, text= "Auto click score gain per click: " + str(auto_click_increment * auto_click_multiplier), font=("Courier", 20))

increment_button = Button(main_window, text= "CLICK HERE", font=("Courier", 15), command=increase_score)
increment_button.place(x=250,y=300)

open_save_window = Button(main_window, text="Save", font=("Courier", 15), command=open_saves)
open_save_window.place(x=250,y=400)

open_load_window = Button(main_window, text="Load", font=("Courier", 15), command=open_loads)
open_load_window.place(x=250,y=450)

shop_button = Button(main_window, text= "SHOP", font=("Courier", 15), command=open_shop)
shop_button.place(x=250,y=350)

# shop window elements

global shop_score # must be global to update both windows
shop_score = Label(shop_window, text= "Your score: " + str(score_value), font=("Courier", 15))
shop_score.pack(side=TOP)
alert = Label(shop_window, text= "", font=("Courier", 15), fg="red") # initially not shown

# shop window buy buttons

option1 = Button(shop_window, text="Score gain per click +1, Price: 25",  font=("Courier", 10), width=45, command=lambda: buy(25, lambda: increment_increase(1), option1, alert))
option2 = Button(shop_window, text="Double click multiplier, Price: 50", font=("Courier", 10), width=45, command=lambda: buy(50, lambda: multiplier_increase(2), option2, alert)) # lambda delays effect until prerequisite is met
option3 = Button(shop_window, text="Auto click every second (+1/s), Price: 100", font=("Courier", 10), width=45, command=lambda: [buy(100, lambda:auto_click(1000, 1), option3, alert),ac_score_per_click.place(x=100, y=150)])
option3.pack(side=BOTTOM)
option2.pack(side=BOTTOM)
option1.pack(side=BOTTOM)

# save window buttons

save_alert = Label(save_window, text="", font=("Courier", 10), fg="red")
file1 = Button(save_window, text="Save to file 1", font=("Courier", 15), command=lambda: save_file("file1", save_alert))
file2 = Button(save_window, text="Save to file 2", font=("Courier", 15), command=lambda: save_file("file2", save_alert))

file2.pack(side=BOTTOM)
file1.pack(side=BOTTOM)


# window loop and additional function calls

time()
mainloop()
