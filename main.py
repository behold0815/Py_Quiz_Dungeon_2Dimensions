# this is a python practice project "two-dimension quiz dungeon"
# This app will use "CLASS".

from modules.Interact import Interact as INA
from modules.DungeonSettings import DungeonSettings
import json
import os
from logger import logger

# ask if player wants to play this game
INA().askIfWantToPlay()

print("Welcome to Quiz Dungeon!!")
print("You can press 'Ctrl + C' to Exit Dungeon anytime.")
print("Press any key when you are ready to start the adventure!!!")
os.system("pause")
print("You've entered Quiz Dungeon.")

# build dungeon
ds = DungeonSettings()
d = ds.buildDungeon()
xPos, yPos = ds.getPos()
nowPosition = d[xPos][yPos]

# print(f"You are at [{xPos}][{yPos}] position.\n")

while nowPosition != "E":  # now position is not exit
    if nowPosition == "1":
        print("It is an empty room.\n")

    # encounter the quiz
    elif nowPosition == "Q":
        quiz = json.loads(ds.createQuiz())

        while True:
            print("You encounter a quiz room. Please answer the question below:")

            answer = input(quiz['Question'])

            if answer == str(quiz['Answer']):
                print("Your answer is correct.\n")
                break
            else:
                print("Your answer is incorrect.\n")
                continue

    # check 4 directions and add head up
    xPos, yPos = ds.getPos()

    # print(xPos,yPos)
    AD.clear()
    AD = allowedDirection = ['log']
    AD.append(ds.isIndexValid(xPos-1, yPos, 'n', 'North'))
    AD.append(ds.isIndexValid(xPos+1, yPos, 's', 'South'))
    AD.append(ds.isIndexValid(xPos, yPos+1, 'e', 'East'))
    AD.append(ds.isIndexValid(xPos, yPos-1, 'w', 'West'))

    # check if input choice is correct?
    while True:
        print("You need to move to next room.")
        print(ds.headUp)
        headTo = input("What is your choice? ")
        if headTo in AD:
            break
        else:
            print("You entered a wrong choice.\n")

    ds.headUp = ""

    # update now position depends on what key player pressed
    if headTo == "n":
        nowPosition = ds.updateNowPos(xPos-1, yPos)
        logger.writeLog(f"head to N,{xPos-1, yPos}")
    if headTo == "s":
        nowPosition = ds.updateNowPos(xPos+1, yPos)
        logger.writeLog(f"head to N,{xPos+1, yPos}")
    if headTo == "e":
        nowPosition = ds.updateNowPos(xPos, yPos+1)
        logger.writeLog(f"head to E,{xPos, yPos+1}")
    if headTo == "w":
        nowPosition = ds.updateNowPos(xPos, yPos-1)
        logger.writeLog(f"head to W,{xPos, yPos-1}")
    if headTo == "l":
        logger.showLog()

    # print(f"{xPos},{yPos}")

print("It is an exit. Congratulation, you have passed the Quiz Dungeon.")
quit()
