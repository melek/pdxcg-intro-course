'''
Lab 7: Guess the Number
Assignment by Lionel Di Giacomo
1/28/2020
'''
import random
import string

# A function to collect a valid, positive integer.
def validIntInput(prompt, max_input):
    while True: 
        menu_input = input(prompt)
        if(menu_input.isdigit() == False):
            print("Please guess a positive number.")
            continue
        else:
            menu_input = int(menu_input)
        if(menu_input < 1 or menu_input > max_input):
            print(f"{menu_input} is too big! Pick a number under {max_input}.")
            continue
        else:
            return menu_input            

def getGuessSide(guess, target):
    guess_side_of_target = "Just Right"
    if guess > target:
        guess_side_of_target = "Too high"
    elif guess < target:
        guess_side_of_target = "Too low"
    return guess_side_of_target

def getGuessWarmth(this_guess, last_guess, target):
    guess_warmth = "HOT"
    last_guess_off_by = abs(target - last_guess)
    this_guess_off_by = abs(target - this_guess)
    if last_guess_off_by == this_guess_off_by:
        guess_warmth = "Just as warm as before..."
    elif last_guess_off_by > this_guess_off_by:
        guess_warmth = "Warmer"
    else:
        guess_warmth = "Colder"
    return guess_warmth

# [0] = Difficulty Name
# [1] = Upper bound
# [2] = Guess limit
difficulty_levels = [
    ["Easy10", 10, 5],
    ["Hard10", 10, 3],
    ["Med100", 100, 15],
    ["Hard10", 100, 7]]
    
main_menu = f"""
Guess the Number!
=-=-=-=-=-=-=-=-=
1. Guesser Mode: Guess a number the computer picks
2. Picker Mode:  Pick a number and make the computer guess
3. Quit
"""

while True:
    print(main_menu)
    menu_input = validIntInput("Your choice: ", 3)
    
    if(menu_input == 1):
        # Guesser Mode
        print("\nChoose a difficulty mode!")
        for level_index in range(len(difficulty_levels)):
            print(f"{level_index + 1}. {difficulty_levels[level_index][0]} - {difficulty_levels[level_index][2]} guesses at a number from 1-{difficulty_levels[level_index][1]}")
        difficulty_index = validIntInput("Difficulty Level: ", len(difficulty_levels)) - 1
        difficulty_name = difficulty_levels[difficulty_index][0]
        upper_bound = difficulty_levels[difficulty_index][1]
        guess_limit = difficulty_levels[difficulty_index][2]
        print()
        print(f"""Choose a hint level!
        1. All the hints
        2. Only high/low hints
        3. Only warmth hints
        4. Random - A random hint per guess
        5. Psychic Mode - No Hints!")
        """)
        hint_level = validIntInput("Hint Level: ", 5)
        print()
        guesses_made = 0
        target = random.randint(1, upper_bound)
        while guesses_made < guess_limit:
            player_guess = validIntInput(f"Guess a number from 1 to {upper_bound} ({guess_limit - guesses_made} tries left): ", upper_bound)
            guesses_made += 1
            if player_guess == target:
                if guesses_made == 1:
                    guess_text = "only a SINGLE GUESS.."
                else:
                    guess_text = f"{guesses_made} guesses"
                print(f"Congratulations {player_guess} is the number, and it took you {guess_text}. You WIN!")
                print(f"Beaten on {difficulty_name} with hint level {hint_level}.")
                input("Press enter to continue...")
                break
            elif guesses_made > 1:
                guess_side_of_target = getGuessSide(player_guess, target)
                guess_warmth = getGuessWarmth(player_guess, last_guess, target)
                last_guess = player_guess
                random_hint = 0
                if(hint_level == 4):
                    random_hint = random.randint(2,3)
                if(hint_level == 1):
                    print(f"Too {guess_side_of_target} and {guess_warmth}...")
                elif(hint_level == 2 or random_hint == 2):
                    print(f"Too {guess_side_of_target}...")
                elif(hint_level == 3 or random_hint == 3):
                    print(f"Getting {guess_warmth}...")
                else:
                    print("No hint!")
            else:
                guess_side_of_target = getGuessSide(player_guess, target)
                last_guess = player_guess
                if(hint_level == 4):
                    random_hint = random.randint(1,4)
                if(hint_level == 1):
                    print(f"{guess_side_of_target} and guess again for a warmth hint...")
                elif(hint_level == 2 or random_hint == 2):
                    print(f"{guess_side_of_target}...")
                elif(hint_level == 3 or random_hint == 3):
                    print(f"Guess again for a warmth hint...")
                else:
                    print("No hint!")
        else:
            print("Oops.. you ran out of guesses!")
            input("Press enter to continue...")
    elif menu_input == 2:
        # Picker Mode
        target_limit = 10
        guess_limit = 5
        possible_guesses = range(1, target_limit)
        player_target = validIntInput(f"Give the computer a number to guess between 1 and {target_limit} - it will have 5 guesses: ")
        print("Possible Guesses = " + possible_guesses)
    
    elif menu_input == 3 :
        break

print("Goodbye!")