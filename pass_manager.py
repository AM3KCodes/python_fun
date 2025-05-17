from tkinter import *
from tkinter import filedialog
from cryptography.fernet import *
import json

# global variables

last_key = ""

# main window

main_window = Tk()
main_window.geometry("700x500")
main_window.title("Password Manager")
main_window.resizable(False,False)

# encryption/decryption window

ed_window = Toplevel()
ed_window.geometry("500x350")
ed_window.title("Encryption/Decryption")
ed_window.resizable(False, False)
ed_window.withdraw()
ed_window.protocol("WM_DELETE_WINDOW", ed_window.withdraw)

# methods

# load
def load():
    path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    
    if path:
        with open (path, 'r') as file:
            try:
                global data
                data = json.load(file)
                
                length = data["length"]
                isc = data["included_special_characters"]
                ist = data["included_specific_terms"]
                pot = data["position_of_term"]
                st = data["specific_term"]
                password = data["password"]

                # debug text
                print("Length: " + str(length) + "\n"  
                    + "Included special characters: " + str(isc) + "\n" 
                    + "Included specific term: " + str(ist) + "\n" 
                    + "Position of term: " + str(pot) + "\n" 
                    + "Specific term: " + str(st) + "\n" 
                    + "Password: " + str(password))
                alert.configure(text="File has been loaded.")
                alert.pack(side=BOTTOM)
            except json.JSONDecodeError:
                alert.configure(text="File could not be loaded.")
                alert.pack(side=BOTTOM)
            alert.after(5000, lambda: alert.destroy())

# create key
def get_key():
    global last_key
    last_key = Fernet.generate_key()
    key_label.configure(text=str(last_key))
    key_label.pack(side=BOTTOM)
    return last_key
            
# copy    
def copy(last_key):
    main_window.clipboard_clear()
    main_window.clipboard_append(last_key)
    main_window.update()
    if last_key != "":
        key_label.configure(text="Key has been copied to clipboard.")
    else:
        key_label.configure(text="No key has been generated yet.")
    key_label.after(5000, lambda: key_label.destroy())

# encryption
def encrypt(data):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(str(data["password"]).encode())
    if encrypted_password:
        key_label.configure(text=f"Password has been encrypted: {encrypted_password}")
    return encrypted_password
            
# main window elements

Label(main_window, text="Decryptor/Encryptor", font=("Bahnschrift", 30)).pack(side=TOP)
Label(main_window, text="Select a file to load.", font=("Bahnschrift", 20)).pack(side=TOP)

alert = Label(main_window, text="", font=("Bahnschrift", 7), fg="red")
file_select = Button(main_window, text="Open File", font=("Bahnschrift", 10), command=lambda: load())
file_select.pack(side=TOP)

key_label = Label(main_window, text="", font=("Bahnschrift", 10), fg="green")
create_key = Button(main_window, text="Generate Encryption Key", font=("Bahnschrift", 10), command=lambda: get_key())
create_key.pack(side=TOP)

copy_key = Button(main_window, text="Copy Encryption Key", font=("Bahnschrift", 10), command=lambda: copy(last_key))
copy_key.pack(side=TOP)

open_ed = Button(main_window, text="Open Encryption/Decryption Window", font=("Bahnschrift", 10), command=lambda:ed_window.deiconify())
open_ed.pack(side=TOP)

key = StringVar()
key_entry = Entry(ed_window, textvariable = key, font=("Bahnschrift", 10), show="*")
key_entry.pack(side=TOP)




main_window.mainloop()
