'''
Lab 1: Hello
Assignment by Lionel Di Giacomo
1/21/2020

This introductory 'lab' was just testing essential language constructs.
'''
# This is a single line comment in python. It is useful for ignoring a line of code quickly.

# Prints to the terminal the provided string on a new line. 
print("Hello World!")

'''
    This is a long python comment.
    It can be multiple lines long, but it doesn't have to be.
'''

""" Double quotes create comments as well. """

# Variable declaration
greeting = "I hope you are all having a great day!"

# Simple for loops
for x in range(5):
    # Casting a string to int for concatenation
    print(str(x) + ": " + greeting)

Mouse = "mickey"
cat = "garfield"
print(f"{Mouse} ran away from {cat}")
