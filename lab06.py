'''
Lab 6: Rock Paper Scissors
Assignment by Lionel Di Giacomo
1/23/2020
'''
import random

weapons = {
    0: "rock", 
    1: "paper", 
    2: "scissors"}
computerWins = 0
playerWins = 0
gameRound = 1

def printWeaponMenu():
    print("Choose your weapon:")
    for i in range(len(weapons)):
        print(f"{i}: {weapons[i]}")        

print("Welcome to Rock Paper Scissors!")
lastWeapon = random.randint(0, len(weapons) - 1)
menuChoice = -1
while menuChoice != "q":
    print(f"\nRound {gameRound}...")
    printWeaponMenu()

    while True:
        menuChoice = input("Choose your weapon (or 'q' to quit): ").lower()
        if menuChoice == "":
            menuChoice = lastWeapon
        elif menuChoice =="q":
            print(f"\nQuitting... \n\nYou played {gameRound-1} rounds!")
            playerGameWord = "game" if playerWins == 1 else "games"
            computerGameWord = "game" if computerWins == 1 else "games"
            tieGames = gameRound - 1 - playerWins - computerWins
            tieGameWord = "game" if tieGames == 1 else "games"
            
            print(f"You won {playerWins} {playerGameWord}, and the computer won {computerWins} {computerGameWord}. ", end = "")
            print(f"You tied {tieGames} {tieGameWord}.")
            print("Goodbye, thanks for playing!")
            exit()
        elif menuChoice in ["0", "1", "2"]:
            menuChoice = int(menuChoice)
            break
    
    playerWeapon = menuChoice
    lastWeapon = playerWeapon
    menuChoice = -1

    print(f"\nYou chose {weapons[playerWeapon]}...")

    computerWeapon = random.randint(0,len(weapons) - 1)
    print(f"The computer chose {weapons[computerWeapon]}")

    if computerWeapon == playerWeapon:
        print(f"{weapons[computerWeapon]} can't beat itself...")
        print("Its a tie!")
        gameRound += 1
    elif computerWeapon == 0 and playerWeapon == len(weapons) -1:
        print(f"{weapons[computerWeapon]} beats {weapons[playerWeapon]}.")
        print("Sorry, you lose!")
        computerWins += 1
        gameRound += 1
    elif playerWeapon == 0 and computerWeapon == len(weapons) -1:
        print(f"{weapons[playerWeapon]} beats {weapons[computerWeapon]}.")
        print("Congratulations, you WIN!")
        playerWins += 1
        gameRound += 1
    elif computerWeapon > playerWeapon:
        print(f"{weapons[computerWeapon]} beats {weapons[playerWeapon]}.")
        print("Sorry, you lose!")
        computerWins += 1
        gameRound += 1
    elif playerWeapon > computerWeapon:
        print(f"{weapons[playerWeapon]} beats {weapons[computerWeapon]}.")
        print("Congratulations, you WIN!")
        playerWins += 1
        gameRound += 1
    else:
        print("Not sure what happened...")
        
print("Mysterious... you got out of the main loop in a way I didn't except. Goodbye!")
