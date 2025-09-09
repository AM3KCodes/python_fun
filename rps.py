import random
import time


# main menu
def main_menu():
    print("Welcome to RPS.")
    print("1. Play")
    print("2. CPU vs CPU")
    print("3. Recursive CPU Play")
    choice = input("Select an option (1, 2, or 3):\n")
    if choice == '1':
        play()
    elif choice == '2':
        cpu_v_cpu()
    elif choice == '3':
        trials = int(input("Enter amount of trials to run:\n"))
        if trials <= 0:
            print("Trial number cannot be less than or equal to 0. Returning to main menu.")
            main_menu()
        else:
            print(f"Running {trials} trials.")
            time.sleep(1)
            print(f"Running {trials} trials..")
            time.sleep(1)
            print(f"Running {trials} trials...")
            recursive_play(trials)
            print("Trials completed. Returning to main menu.")
            main_menu()

""""CHOICE FUNCTION SECTION START"""

def player_choice():
    while True:
        choice = input("Press 1 for rock, 2 for paper, 3 for scissors\n")
        if choice in ('1', '2', '3'):
            choice = int(choice)
            if choice == 1:
                print("Rock chosen.")
            elif choice == 2:
                print("Paper chosen.")
            elif choice == 3:
                print("Scissors chosen.")
            elif choice == 4:
                print("Computer vs Computer mode chosen.")
            return choice
        else:
            print("Invalid input, please try again.")

def opponent_choice():
    opp_choice = random.randint(1, 3)
    if opp_choice == 1:
        print("Rock chosen by opponent.")
    elif opp_choice == 2:
        print("Paper chosen by opponent.")
    elif opp_choice == 3:
        print("Scissors chosen by opponent.")
    return opp_choice

def ally_cpu_choice():
    ally_choice = random.randint(1,3)
    if ally_choice == 1:
        print("Rock chosen by ally.")
    elif ally_choice == 2:
        print("Paper chosen by ally.")
    elif ally_choice == 3:
        print("Scissors chosen by ally.")
    return ally_choice

"""CHOICE FUNCTION SECTION END"""

# general replay function
def play_again():
    option = input("Play again? (Y/N):\n").capitalize()
    if option == "Y":
        play()
    else:
        menu_option = input("Return to main menu? (Y/N):\n").capitalize()
        if menu_option == "Y":
            main_menu()
        else:
            exit()    
        
# play again specifically for computer vs computer mode, eventually adding conditional to play_again() to reduce redundancy
def play_again_cpu():
    option = input("Play again? (Y/N):\n").capitalize()
    if option == "Y":
        cpu_v_cpu()
    else:
        menu_option = input("Return to main menu? (Y/N):\n").capitalize()
        if menu_option == "Y":
            main_menu()
        else:
            exit() 

# recursive play function
def recursive_play(trials):
    for i in range(trials):
        print(f"Trial {i+1}:")
        time.sleep(1)
        cpu_v_cpu_repeatable()
        time.sleep(1)
        if i == trials:
            print("All trials completed. Returning to main menu.")
            main_menu()

"""GAME MODE FUNCTION SECTION START"""

# recursive computer vs computer mode
def cpu_v_cpu_repeatable():
    ally = ally_cpu_choice()
    print("Opponent is deciding.")
    time.sleep(1)
    print("Opponent is deciding..")
    time.sleep(1)
    print("Opponent is deciding...")
    time.sleep(1)
    opponent = opponent_choice()
    if ally == opponent:
        print("Tie!")
    elif (ally == 1 and opponent == 3) or (ally == 2 and opponent == 1) or (ally == 3 and opponent == 2):
        print("Ally computer wins!")
    else:
        print("Ally computer loses!")  


# computer vs computer mode
def cpu_v_cpu():
    ally = ally_cpu_choice()
    print("Opponent is deciding.")
    time.sleep(1)
    print("Opponent is deciding..")
    time.sleep(1)
    print("Opponent is deciding...")
    time.sleep(1)
    opponent = opponent_choice()
    if ally == opponent:
        print("Tie!")
    elif (ally == 1 and opponent == 3) or (ally == 2 and opponent == 1) or (ally == 3 and opponent == 2):
        print("Ally computer wins!")
    else:
        print("Ally computer loses!")
    play_again_cpu()
    
# single player mode
def play():
    player = player_choice()
    print("Opponent is deciding.")
    time.sleep(1)
    print("Opponent is deciding..")
    time.sleep(1)
    print("Opponent is deciding...")
    time.sleep(1)
    opponent = opponent_choice()
    if player == opponent:
        print("Tie!")
    elif (player == 1 and opponent == 3) or (player == 2 and opponent == 1) or (player == 3 and opponent == 2):
        print("You win!")
    else:
        print("You lose! Try again.")
    play_again()
    
"""GAME MODE FUNCTION SECTION END"""

# execute program
main_menu()