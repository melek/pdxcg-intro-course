'''
Lab 2: Mad Libs
Assignment by Lionel Di Giacomo
1/21/2020
'''

noun1 = input("Give me an animal: ")
preposition = input("And a preposition...: ")
nounProper1 = input("And a proper noun...: ")
adjective = input ("And an adjective... : ")
nounInanimate = input("And any inanimate object...: ")
nounBodyPart = input("And any body part...: ")
nounPlace = input("And finally, a location or type of place: ")
madlib = f"""
The {noun1} snuck into {nounProper1}'s {nounPlace} and stole their {adjective} {nounInanimate} from right {preposition} their {nounBodyPart}!
"""

print(madlib)