# clicker (key press) game
import keyboard

def main():
    game_start()

def game_start():
    while True:
        current_money = 1 # initial amount of money
        multiplier = 1 # initial multiplier
        gain_on_key_press = 1 # initial money gain
        print(f"Current money: {current_money}\nMultiplier: {multiplier}\nGain on press: {gain_on_key_press}")
        if keyboard.is_pressed('f'):
            return gain_money(current_money, multiplier, gain_on_key_press)

def gain_money(current_money, multiplier, gain_on_key_press):
    current_money = current_money + (gain_on_key_press * multiplier)
    return current_money

def shop(current_money):
    shop = []
    return
