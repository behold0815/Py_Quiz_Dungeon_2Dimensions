# this is a python practice project "two-dimension quiz dungeon"
# This app will use "CLASS".
# 建立走過的路線地圖

from modules.Interact import Interact
from modules.DungeonSettings import DungeonSettings
import json
from logger import logger

# ask if player wants to play this game
INA = Interact()
INA.askIfWantToPlay()
INA.welcomeWords()

# build dungeon
ds = DungeonSettings()
d = ds.buildDungeon()
xPos, yPos = ds.getPos()
PositionContent = d[xPos][yPos]
rMap = d.copy() # copy dungeon and record the map you passed by

# print(f"You are at [{xPos}][{yPos}] position.\n")

while PositionContent != "E":  # now position is not exit
    if PositionContent == "1":
        print("It is an empty room.\n")

    # encounter the quiz
    elif PositionContent == "Q":
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
    AD = allowedDirection = []
    AD.clear()
    AD = ['log']
    AD.append(ds.isIndexValid(xPos-1, yPos, 'n', 'North'))
    AD.append(ds.isIndexValid(xPos+1, yPos, 's', 'South'))
    AD.append(ds.isIndexValid(xPos, yPos+1, 'e', 'East'))
    AD.append(ds.isIndexValid(xPos, yPos-1, 'w', 'West'))

    # check if input choice is correct?
    while True:
        print("You need to move to next room.")
        print(ds.headUp)
        print("Press 'log' to read log.; 'map' to read map.")
        headTo = input("What is your choice? ")
        if headTo in AD:
            break
        else:
            print("You entered a wrong choice.\n")

    ds.headUp = ""

    # update now position depends on what key player pressed
    if headTo == "n":
        PositionContent = ds.updateNowPos(xPos-1, yPos)
    if headTo == "s":
        PositionContent = ds.updateNowPos(xPos+1, yPos)
    if headTo == "e":
        PositionContent = ds.updateNowPos(xPos, yPos+1)
    if headTo == "w":
        PositionContent = ds.updateNowPos(xPos, yPos-1)
    if headTo == "log":
        headsUp = "You are watching log. It's when and where you've been to in dungeon."
        INA.disPlay(headsUp,logger.showLog) # pass ds.showLog by address
    if headTo == "map":
        headsUp = "This is the map you've passed through."
        # INA.disPlay(headsUp,)

    # check 4 directions and add head up
    xPos, yPos = ds.getPos()
    # print(f"{xPos},{yPos}")

print("It is an exit. Congratulation, you have passed the Quiz Dungeon.")
quit()
