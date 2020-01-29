'''
Lab 5: Random Emoticon Generator
Assignment by Lionel Di Giacomo
1/23/2020
'''
import random

eyebrows = ["",">","<"]
eyes = [":",";","8","B"]
noses = [""," ","-","^","*"]
mouths = [")","}","]","|","(","{","[","D","C","O","o","S","/"]

wide_tall_eyes = ["^", "-", "o", "O", ">", "<", "."]
wide_mouths = ["_", "__", ",_,", "_____"]

tall_noses = [" | ", " + ", " @" , " * "]
tall_mouths = ["___", " _ ", " U ", " ^ ", " - ", "---", " o ", " O "]

faces = len(eyebrows) * len(eyes) * len(noses) * len(mouths)
wide_faces = len(wide_tall_eyes) * len(wide_tall_eyes) * len(wide_mouths)
tall_faces = len(wide_tall_eyes) * len(wide_tall_eyes) * len(tall_noses) * len(tall_mouths)

max = faces + wide_faces + tall_faces

def getFaceChoice(facePartArray, facePartName):
    userChoice = -1
    while userChoice < 0 or userChoice > len(facePartArray):
        for i in range(len(facePartArray)):
            print(f"{i}: {facePartArray[i]}")
        userChoice = int(input(f"Choose your {facePartName}: "))
    return facePartArray[userChoice]

print(f""" ----- Welcome to the Emoticon Generator -----

         Now with {max} possible faces!!""")

menuChoice = "0"
printMenu = True

while menuChoice != "5" and menuChoice != "q" and menuChoice != "bye":
    if(printMenu == True):
        print(f"""
    Menu
    ----
    1: Generate 5 random standard emoticons
    2: Generate 3 random wide emoticons
    3: Generate 1 random tall emoticon
    4: Create your own!
    5: Quit (or type 'bye')\n""")
        printMenu = False
    
    newChoice = input("What would you like to do? (hit 'enter' to repeat the last command, 0 for the menu)'): ").lower()
    if(newChoice != ""):
        menuChoice = newChoice

    if(menuChoice == "0"):
        printMenu = True

    elif(menuChoice == "1"):
        # 5 random standard emoticons
        print()
        for i in range(5):
            face = random.choice(eyebrows) + random.choice(eyes) + random.choice(noses) + random.choice(mouths)
            print(face)
        print()

    elif(menuChoice == "2"):
        # 3 random wide emoticons
        print()
        for i in range(3):
            face = random.choice(wide_tall_eyes) + random.choice(wide_mouths) + random.choice(wide_tall_eyes)
            print(face)
        print()

    elif(menuChoice == "3"):
        # 1 random tall emoticon
        print("\n" + random.choice(wide_tall_eyes) + " " + random.choice(wide_tall_eyes))
        print(random.choice(tall_noses))
        print(random.choice(tall_mouths) + "\n")

    elif(menuChoice == "4"):
        # Create your own
        subMenuChoice = ""
        while(subMenuChoice != "1" and subMenuChoice != "2" and subMenuChoice != "3"):
            subMenuChoice = input("""What kind of emoticon would you like?
1: standard :)
2: wide ^_^
3: tall  ^ ^
          |
         ___         

Choose 1-3 or hit 'enter' for a random type: """).lower()
            if subMenuChoice == "":
                subMenuChoice == random.randint(1,3)
            elif subMenuChoice in ["q", "0", "bye", "5"]:
                print(f"Quitting Emoticon creator early... ({subMenuChoice})")
                break
        else:
            if subMenuChoice == "1":
                # Construct Normal Emoticon
                eyebrowChoice = getFaceChoice(eyebrows, "eyebrows")
                eyeChoice = getFaceChoice(eyes, "eyes")
                noseChoice = getFaceChoice(noses, "nose")
                mouthChoice = getFaceChoice(mouths, "mouth")
                userFace = f"{eyebrowChoice}{eyeChoice}{noseChoice}{mouthChoice}"
                print(f"Meet your new emoticon!\n\n   {userFace}\n\nHope you like it :)")

            elif subMenuChoice == "2":
                # Construct Wide Emoticon
                eye1Choice = getFaceChoice(wide_tall_eyes, "left eye")
                eye2Choice = getFaceChoice(wide_tall_eyes, "right eye")
                mouthChoice = getFaceChoice(wide_mouths, "mouth")
                userFace = f"{eye1Choice}{mouthChoice}{eye2Choice}"
                print(f"Meet your new emoticon!\n\n   {userFace}\n\nHope you like it :)")

            elif subMenuChoice == "3":
                # Construct Tall Emoticon
                eye1Choice = getFaceChoice(wide_tall_eyes, "left eye")
                eye2Choice = getFaceChoice(wide_tall_eyes, "right eye")
                noseChoice = getFaceChoice(tall_noses, "mouth")
                mouthChoice = getFaceChoice(tall_mouths, "mouth")
                userFace = f"   {eye1Choice} {eye2choice}\n   {mouthChoice}\n   {eye2Choice}"
                print(f"Meet your new emoticon!\n\n{userFace}\n\nHope you like it :)")

    elif menuChoice == "5" or menuChoice == "q" or menuChoice == "bye":
        # Quitting
        continue

    else:
        # Invalid input
        "Invalid selection. Please enter a menu choice! (1-5 or 'q')"
else:
    print("Goodbye!")