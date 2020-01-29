'''
Lab 8: Password Generator
Assignment by Lionel Di Giacomo
1/28/2020
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


max_chars_of_single_type = 256

print("Let's make you a killer password!")
letters = validIntInput("How many letters? ", max_chars_of_single_type)
numbers = validIntInput("How many numbers? ", max_chars_of_single_type)
punctuation = validIntInput("How many punctuation characters? ", max_chars_of_single_type)
max_length = letters + numbers + punctuation

max_length_override = validIntInput(f"Right now your password will be {max_length}. Hit 'Enter' to accept this password length, or enter a different length (max {max_chars_of_single_type * 3}): ", max_chars_of_single_type * 3, max_length)

if(max_length != max_length_override):
    letters = round( letters / max_length * max_length_override )
    numbers = round( numbers / max_length * max_length_override ) 
    punctuation = round( punctuation / max_length * max_length_override )

    if(max_length > max_length_override):
        transformation_word = "clamped"
    else:
        transformation_word = "expanded" 
    print(f"Your password will be {transformation_word} to {max_length_override} but will retain the proportion of letters, numbers, and punctuation you specified.")

max_length = max_length_override
calculated_max_length = letters + numbers + punctuation

while(calculated_max_length != max_length):
    print("There was a rounding issue with the max_length of the password...", end="")
    if calculated_max_length < max_length:
        print(" adding a letter.")
        letters += 1    
    else:
        print(" removing a letter.")
        letters -= 1
    calculated_max_length = letters + numbers + punctuation

password = []
for i in range(letters):
    password.append(random.choice(string.ascii_letters))
for i in range(numbers):
    password.append(random.choice(string.digits))
for i in range(punctuation):
    password.append(random.choice(string.punctuation))

random.shuffle(password)

print(f"Your password is: \n\n{''.join(password)}\n")