# this is a python practice project "two-dimension quiz dungeon"
# This app will use "CLASS".
# 建立走過的路線地圖

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
xPos = 0
yPos = 0
PositionContent = d[xPos][yPos]

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
        headTo = input("What is your choice? ")
        if headTo in AD:
            break
        else:
            print("You entered a wrong choice.\n")

    ds.headUp = ""

    # update now position depends on what key player pressed
    if headTo == "n":
        PositionContent,xPos,yPos = ds.updateNowPos(d, xPos-1, yPos)
    if headTo == "s":
        PositionContent,xPos,yPos = ds.updateNowPos(d, xPos+1, yPos)
    if headTo == "e":
        PositionContent,xPos,yPos = ds.updateNowPos(d, xPos, yPos+1)
    if headTo == "w":
        PositionContent,xPos,yPos = ds.updateNowPos(d, xPos, yPos-1)
    if headTo == "log":
        os.system("cls")
        print("You are watching log. It's when and where you've been to in dungeon.")
        ds.showLog()
        os.system("pause")

    # print(f"{xPos},{yPos}")

print("It is an exit. Congratulation, you have passed the Quiz Dungeon.")
quit()
