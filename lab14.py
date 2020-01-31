'''
Lab 14: Turtle Showcase 
Assignment by Lionel Di Giacomo
1/30/2020
'''
import random
import string

# A function to collect a valid, positive integer.
def validIntInput(prompt, max_input, default = None):
    while True: 
        menu_input = input(prompt)
        if menu_input == "" and default != None:
            return int(default)
        elif(menu_input.isdigit() == False):
            print("Please guess a positive number.")
            continue
        else:
            menu_input = int(menu_input)
        if(menu_input < 1 or menu_input > max_input):
            print(f"{menu_input} is too big! Pick a number up to {max_input}.")
            continue
        else:
            return menu_input

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()