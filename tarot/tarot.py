from math import floor
from tarotDict import majorDict, minorNumDict, minorSuitDict

# Method to get the specified card as a string
def getCardName(card):
    if card < 0: 
        card *= -1

    if card >= 78:
        card %= 78    

    if card <= 21:  
        cardName = majorDict[card]
    elif card <= 77:
        cardNum =  minorNumDict[(card - 22) % 14]
        suitIndex = int(floor((card - 22) / 14))
        if(suitIndex > len(minorSuitDict)):
           suitIndex = suitIndex % 4
        cardSuit = minorSuitDict[suitIndex]
        cardName = f"the {cardNum} of {cardSuit} ({card})"
    else:
        cardName = "not a tarot card.. wierd"
    return cardName

# This method converts a provided string to an integer and returns a card number. 

def lazyCard(anyString):
    questionValue = 0
    for letter in anyString.lower():
        questionValue = questionValue + ord(letter)
    card = questionValue % 78
    return card