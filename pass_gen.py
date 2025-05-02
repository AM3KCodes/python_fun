import random
import string
from tkinter import *

# create password based on user input

def generator(length, isc):
    if isc==False:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return password
    if isc==True:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        return password

while True:
    try:
        length = int(input("Enter the length of your password: "))
        if length <= 0:
            print("Length less than 1, exiting application.")
            break
    except ValueError: # check for invalid inputs
        print("Please enter a valid number.")
        continue
    
    option = input("Include special characters? (Y/N): ").upper()
    if (option=="Y"):
        isc = True
    elif (option=="N"):
        isc = False
    else:
        print("Invalid input. Enter Y or N.")
        continue
        
    print("Password: ", generator(length, isc))
    break
        