# set dungeon, check position, get position
from modules.dateTimeFormat import dateTimeFormat
import numpy as npy
import random
import json
from logger import logger

class DungeonSettings():

    def __init__(self):
        startX = 0  # default x-axis index
        startY = 0  # default y-axis index
        self.xPos = startX  # now position x-axis index
        self.yPos = startY  # now position y-axis index
        self.dungeon = npy.array( # dungeon layout
            [["Q", "1", "1", "0", "0", "2", "0", "0", "0", ],
             ["1", "0", "1", "0", "0", "1", "0", "2", "0", ],
             ["1", "1", "1", "0", "0", "1", "0", "1", "0", ],
             ["0", "1", "Q", "1", "1", "1", "1", "1", "E", ],
             ["2", "1", "0", "0", "0", "0", "0", "0", "0", ],
             ["0", "1", "0", "1", "Q", "1", "1", "2", "0", ],
             ["0", "1", "0", "1", "0", "1", "0", "0", "0", ],
             ["0", "1", "0", "1", "0", "1", "0", "E", "0", ],
             ["0", "1", "Q", "1", "0", "1", "1", "1", "0"]]
        )
        self.Dung = self.buildDungeon()
        self.xMax, self.yMax = self.Dung.shape  # get dungeon shape
        self.headUp = ""
        self.rMap = npy.full((self.xMax,self.yMax), " ").tolist()
        self.roomSettings = {
            "0": "wall",
            "1": "empty",
            "2": "dead end",
            "E": "exit",
            "Q": "quiz",
        }
        self.Quiz = [
            {"Question": "1+1=", "Answer": 2},
            {"Question": "5+1=", "Answer": 6},
            {"Question": "3+1=", "Answer": 4},
            {"Question": "11+1=", "Answer": 12}
        ]

    # get now position x,y index
    def getPos(self):
        return self.xPos, self.yPos

    # create quiz
    def createQuiz(self):
        return json.dumps(random.choice(self.Quiz))

    # build dungeon
    def buildDungeon(self):
        return self.dungeon

    # check if the index in "2D array" is out of range
    def posIsValid(self, xPo, yPo):
        if xPo < 0 or yPo < 0 or xPo >= self.xMax or yPo >= self.yMax:
            return False
        return True

    # check if index is valid
    def isIndexValid(self, xPos, yPos, key, direction):
        d = self.Dung
        # check if the index is not out of range
        if self.posIsValid(xPos, yPos) == True:
            room = d[xPos][yPos]  # update certain direction index
            if room != "0":  # if the room is not "Wall"
                self.updateHeadUp(key, direction)
                return key
        return "null"

    # update now position
    @logger.writeLog
    def updateNowPos(self, xPos, yPos, headTo):
        nowPosition = self.Dung[xPos][yPos]  # update 4 directions index
        self.xPos = xPos
        self.yPos = yPos
        self.recordMap(headTo,xPos,yPos)
        return nowPosition # if method return anything, you must use return

    # update head-up
    def updateHeadUp(self, key, direction):
        if self.headUp != "":
            self.headUp += "\n"
        self.headUp += f"Press '{key}' head to {direction}."

    # record map the player passed through
    def recordMap(self, headTo, xPos, yPos):
        # ▲▼✱▶◀？☐
        marks = {
            "n":"↑",
            "s":"↓",
            "e":"→",
            "w":"←",
            "pass again":"✱",
            "Q":"？",
            "E":"☐"
        }

        conT = self.Dung[xPos][yPos]
        rMapCont = self.rMap[xPos][yPos]

        if conT == "Q" or conT == "E":
            rMapCont = marks[conT]
        # elif rMapCont != " ":
        #     rMapCont = marks["pass again"]
        else:
            rMapCont = marks[headTo]

        self.rMap[xPos][yPos] = rMapCont

    def showMap(self):
        for i in self.rMap:
            for j in i:
                print(j,end="")
            print("")



# # a Directions Heads Up
# aDirectionsHeadsUp = [
#     {"Left":"Your left is "},
#     {"Right":"Your right is "},
#     {"Front":"Your front is "},
#     {"Back":"You have back to the original path "},
# ]

# # a Environment Heads Up
# aEnvironmentHeadsUp = [
#     {"0":"wall that you cannot pass. "},
#     {"1":"a path that you can pass. "},
#     {"2":"the exit that means you passed the Quiz journey. "},
#     {"Q":"a question you need to solve. "}
# ]

