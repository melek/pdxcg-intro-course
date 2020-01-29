""" 
    Give the user a lucky card by smushing together their birthday.
"""
import tarot

name = str(input("Hello and Welcome to Baba Python, your digital fortune teller!\nWhat is your name, please? "))

menu_choice = 0

main_menu = f"""
Hello {name}! Let me draw you a Tarot card.

Here are the kinds of readings I can offer.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
1. Ask a specific question...
2. Get your lucky birthday card...
3. Just draw a random card...
4. Exit, I don't need a reading.")
"""
import random

print(main_menu)
while menu_choice != 4:
    menu_choice = input("Please, make your choice (1-4): ")
    if(menu_choice.isdigit()):
        menu_choice = int(menu_choice)
    else:
        print(main_menu)
        continue

    if menu_choice == 1 or menu_choice == 2 or menu_choice == 3:
        if menu_choice == 1:
            prompt = "What is your question?: "
            question_prefix = name + " asks "
        elif menu_choice ==2:
            prompt = "When is your birthday?: "
            question_prefix = "For " + name + "'s birthday "
        else:
            prompt = ""
            card = random.randint(0, 77)
        if prompt != "":
            question = question_prefix + str(input(prompt))
            card = tarot.lazyCard(question)
            print(question)
        print(f"Hmm... {name}, your card is {tarot.getCardName(card)}!")

    elif menu_choice == 3:
        print("Coming Soon!")
    elif menu_choice == 4:
        break
print("Goodbye!")