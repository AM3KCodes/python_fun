import random
import string
from tkinter import *
import json

# create password based on user input 

def generator(length, isc, ist, position, specific_term):
    
    # If specific term...
    if ist and position == "START":
        length -= len(specific_term)
        # If special chars...
        if isc:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        # If no special chars...
        else:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return specific_term + password
    
    if ist and position == "END":
        length -= len(specific_term)
        if isc:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        else:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return password + specific_term
    
    # If there is no specific term, check for special chars...
    if isc:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    else:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return password

# save password to file

def save(file):
    data = {
        "length":length,
        "included_special_characters":isc,
        "included_specific_terms":ist,
        "position_of_term":position,
        "specific_term":specific_term,
        "password":generator(length, isc, ist, position, specific_term)
    }
    path = str(file) + ".json"
    with open(path, 'w') as save_data:
        json.dump(data, save_data, indent=4)

while True:
    
    # CREATING PASSWORD LENGTH
    
    try:
        length = int(input("Enter the length of your password: "))
        if length <= 7:
            print("Length cannot be less than 8. Please enter another value.")
            continue
        elif length > 30:
            print("Length cannot be greater than 30. Please enter another value.")
            continue

    except ValueError: # check for invalid inputs
        print("Please enter a valid number.")
        continue
    
    
    # CREATING SPECIFIC TERM
    
    incl_specific_term = input("Include specific term? (Y/N): ").strip().upper() # specific term check
    if (incl_specific_term=="Y"):
        ist = True
        specific_term = input("Enter your specific term: ") # enter term
        if len(specific_term) >= length:
            print("Specific term's length cannot exceed length of the password. Restarting...")
            continue
        position = input("Enter the position of the specific term (START/END): ").strip().upper() # position of specific term
        
    elif (incl_specific_term=="N"):
        ist = False
        specific_term = ""
        position = "START"
    else:
        print("Invalid input. Enter Y or N. Restarting...")
        continue
    
    
    # INCLUDING SPECIAL CHARACTERS
    
    special_characters = input("Include special characters? (Y/N): ").strip().upper() # special characters boolean check
    if (special_characters=="Y"):
        isc = True
    elif (special_characters=="N"):
        isc = False
    else:
        print("Invalid input. Enter Y or N. Restarting...")
        continue
    
    # SAVE PASSWORD

    save_password = input("Save password to file? (Y/N): ").strip().upper()
    if (save_password=="Y"):
        file = input("Enter file name: ")
        save(file)
        print(f"File has been saved to {file}.json.")
    elif (save_password=="N"):
        print("Program completed execution.")
    else:
        print("Invalid input. Enter Y or N. Restarting...")

    # FINAL PASSWORD
    
    print("Password: ", generator(length, isc, ist, position, specific_term))
    break
        