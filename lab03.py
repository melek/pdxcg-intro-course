'''
Lab 3: Magic Eight Ball
Assignment by Lionel Di Giacomo
1/22/2020
'''

"""
Print a welcome screen to the user.
Prompt the user to ask the 8-ball a question.
For example: "Will I win the lottery tomorrow?"
Use the random module's random.choice() to choose a prediction.
Display the result of the prediction.
"""
import random

print("""
                --==*  Welcome to the Python Magic 8-ball *==--
                  -=*   Discover what your future holds!  *=- 
                                    -=**=-
""")

fortuneList = [
    "With perserverence you are sure to succeed!", 
    "Outlook doesn't look good...",
    "Concentrate and ask again!",
    "Don't count on it.",
    "It's not in the cards...",
    "The stars say... YES!",
    "Luck is on your side!"
    ]

question = ""

while question.lower() != "quit":
    question = input("Enter a question or hit 'enter' to get your fortune without typing: ")
    if question.lower() == "quit":
        break

    response = random.choice(fortuneList)
    
    horizontalRule = ""
    for x in range(len(response)):
        horizontalRule = horizontalRule + "-"
    
    print(f"""\n     +=-{horizontalRule}-=+
     |  {response}  |
     +=-{horizontalRule}-=+\n""")

    print("Ask another question, or type 'quit' to put away the eight-ball.")

print("Goodbye!")