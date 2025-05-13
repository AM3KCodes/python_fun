from tkinter import *

from tkinter.filedialog import asksaveasfilename
import string, random

import json

# global variables

password_generated = False
valid_length = False
valid_term = False
valid_input = False
last_password = ""

# functions

def istEntry():
    if ist.get() == True:
        st_text.pack(side=TOP)
        st_entry.pack(side=TOP)
        st_text2.pack(side=TOP)
        st_option.pack(side=TOP)
    else:
        st_text.pack_forget()
        st_entry.pack_forget()
        st_text2.pack_forget()
        st_option.pack_forget()

def copy_to_clipboard(last_password):
    window.clipboard_clear()
    window.clipboard_append(last_password)
    window.update()
    if last_password != "":
        pass_label.configure(text="Password has been copied to clipboard!")
    else:
        pass_label.configure(text="No password has been generated yet. Please generate a password before copying.")
   
def passwordGen(length, isc, ist, selected_position, term):
    global password_generated
    global password
    global final_pass
    global last_password
    global valid_length
    global valid_term
    global valid_input
    valid_length = False # reset validity checks
    valid_term = False
    valid_input = False
    if length <= 30 and length >= 8:
        valid_length = True
    if len(term) <= length:
        valid_term = True
    if (valid_term==True) and (valid_length==True):
        valid_input = True
    # conditional code for "error" involving password lengths above 30
    if (valid_length==False):
        pass_label.configure(text="Password length is less than 8 or greater than 30. Please choose another length.")
        return
    elif (valid_term==False):
    # elif length <= 7:
        pass_label.configure(text="Term length cannot be longer than password length.")
        return
    elif (valid_input==True):
        if ist and selected_position == "START": # include conditional statement for password length and term length comparison
            length -= len(term)
            # If special chars...
            if isc:
                password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
            # If no special chars...
            else:
                password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
           
            final_pass = term + password
            last_password = final_pass
            print(final_pass) # debug print
            pass_label.configure(text=("Your password: " + final_pass))
            if final_pass:
                password_generated = True
            return final_pass
       
        if ist and selected_position == "END":
            length -= len(term)
            if isc:
                password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
            else:
                password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
           
            final_pass = password + term
            last_password = final_pass
            print(final_pass) # debug print
            pass_label.configure(text=("Your password: " + final_pass))
            if final_pass:
                password_generated = True        
            # copy_to_clipboard(final_pass)
            return final_pass
   
    # If there is no specific term, check for special chars...
    if isc:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    else:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    last_password = password
    pass_label.configure(text=("Your password: " + password))
    if password:
        password_generated = True                
    print(password) # debug print
    return password

def save(file, save_alert):
    if (password_generated == True):
        data = {
            "length":length.get(),
            "included_special_characters":isc.get(),
            "included_specific_terms":ist.get(),
            "position_of_term":selected_position.get(),
            "specific_term":term.get(),
            "password":str(last_password)
        }
        path = asksaveasfilename(defaultextension=".json", filetypes=[("JSON files","*.json"), ("All files", "*.*")])
        if path:
            try:
                with open(path, 'w') as file:
                    json.dump(data, file, indent=4)
                    save_alert.configure(text=f"Password has been saved to {path}.")
            except Exception as e:
                    save_alert.configure(text=f"Error saving file: {e}")
            else:
                    save_alert.configure(text="Save has been cancelled. No file has been created.")
    else:
        save_alert.configure(text="No password has been generated yet. Please generate a password before saving.")
    save_alert.pack(side=BOTTOM)
    save_alert.after(5000, lambda: save_alert.destroy())

# main window

window = Tk()
Label(window, text="By: Steven Lau and Paul Basile", font=("Bahnschrift", 7)).pack(side=TOP)

window.title("Random Password Generator")
window.geometry("800x500")
window.resizable(False, False)

# main window elements

pass_label = Label(window, text="Your password: ", font=("Bahnchrift", 10))
pass_label.pack(side=BOTTOM)

positions = ["START", "END"] # for positions dropdown

Label(window, text="Welcome to Random Password Generator!", font=("Verdana", 15)).pack(side=TOP)
# Password length enter...
Label(window, text="Password Length (minimum: 8, maximum: 30): ", font=("Bahnschrift", 17)).pack(side=TOP)
# Enter here...

length = IntVar()
pass_len = Entry(window, width=5, textvariable=length, font = 20)
pass_len.pack(side=TOP)

# Include special characters? Checkbox...
isc = BooleanVar(value=False)
icl_spec = Checkbutton(window, text="Include special characters?", font=("Bahnschrift", 17), variable=isc)
icl_spec.pack(side=TOP)

# Include specific term? Checkbox...
ist = BooleanVar(value=False)
icl_terms = Checkbutton(window, text="Include specific term?", font=("Bahnschrift", 17), variable=ist, command=istEntry)
icl_terms.pack(side=TOP)

# Entry window for when box is checked...
st_text = Label(window, text="Enter term below:", font=("Bahnschrift", 15))
term = StringVar()
st_entry = Entry(window, width=15, textvariable=term, font = 20)

# Positions...
selected_position = StringVar()
selected_position.set(positions[0])
st_text2 = Label(window, text="Position term at start or end of password?", font=("Bahnschrift", 15))
st_option = OptionMenu(window, selected_position, *positions)
st_text.pack_forget()
st_entry.pack_forget()
st_text2.pack_forget()
st_option.pack_forget()


# Generate button...
button = Button(window, text="Generate", fg="green", command=lambda: passwordGen(length.get(), isc.get(), ist.get(), selected_position.get(), term.get()))
button.pack(side=BOTTOM, anchor=CENTER, pady=20)

# Save window button...
file = StringVar()
save_alert = Label(window, text="", font=("Bahnschrift", 7), fg="red")
save_button = Button(window, text="Save", fg="green", command=lambda: save(file.get(), save_alert))
save_button.pack(side=BOTTOM, anchor=CENTER)

# Copy to clipboard button...
copy_button = Button(window, text="Copy Password to Clipboard", fg="green", command=lambda:copy_to_clipboard(last_password))
copy_button.pack(side=BOTTOM, anchor=CENTER, pady=20)
window.mainloop()