from tkinter import *
import string, random
import json

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

def copy_to_clipboard(final_pass):
    window.clipboard_clear()
    window.clipboard_append(final_pass)
    window.update()
    
def passwordGen(length, isc, ist, selected_position, term):
    # conditional code for "error" involving password lengths above 30
    if length > 30:
        pass_label.configure(text="Password length is greater than 30. Please choose another length.")
        return
    elif length <= 7:
        pass_label.configure(text="Password length cannot be less than 8. Please choose another length.")
        return
    else:
        if ist and selected_position == "START": # include conditional statement for password length and term length comparison
            length -= len(term)
            # If special chars...
            if isc:
                password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
            # If no special chars...
            else:
                password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            
            final_pass = term + password
            # if len(final_pass) > length:
            #     pass_label.configure(text="Term length cannot be longer than password length.")
            #     return
            print(final_pass) # debug print
            pass_label.configure(text=("Your password: " + final_pass))
            copy_to_clipboard(final_pass)
            return final_pass
        
        if ist and selected_position == "END":
            length -= len(term)
            if isc:
                password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
            else:
                password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            
            final_pass = password + term
            if len(term) > length:
                pass_label.configure(text="Term length cannot be longer than password length.")
                return
            print(final_pass) # debug print
            pass_label.configure(text=("Your password: " + final_pass))
            copy_to_clipboard(final_pass)
            return final_pass
    
    # If there is no specific term, check for special chars...
    if isc:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    else:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    pass_label.configure(text=("Your password: " + password + " | Copied to clipboard!"))
    print(password) # debug print
    copy_to_clipboard(password)
    return password


window = Tk()
Label(window, text="By: Steven Lau, Paul Basile", font=("Bahnschrift", 7)).pack(side=TOP)

window.title("Random Password Generator")
window.geometry("800x500")
window.resizable(False, False)
# window.configure(bg='lightblue')

pass_label = Label(window, text="Your password: ", font=("Banhschrift", 10))
pass_label.pack(side=BOTTOM)

positions = ["START", "END"]

Label(window, text="Welcome to Random Password Generator!", font=("Verdana", 15)).pack(side=TOP)
# Password length enter...
Label(window, text="Password Length ( 7<x<31 ): ", font=("Bahnschrift", 17)).pack(side=TOP)
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

window.mainloop()
