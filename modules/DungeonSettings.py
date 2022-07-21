# set dungeon, check position, get position

import numpy as npy
import random
import json
from logger import logger


class DungeonSettings:
    def __init__(self):
        startX = 0  # default x-axis index
        startY = 0  # default y-axis index
        quizPassedRoom = [[]]  # recorder the quiz room the player passed
        passedRoom = [[]]  # recorder the room the player passed
        self.xPos = startX  # now position x-axis index
        self.yPos = startY  # now position y-axis index
        self.xMax, self.yMax = self.buildDungeon().shape  # get dungeon shape
        self.headUp = ""
        self.QPR = quizPassedRoom
        self.PRoom = passedRoom

    # get now position x,y index
    def getPos(self):
        return self.xPos, self.yPos

    # create quiz
    def createQuiz(*args):
        Quiz = [
            {"Question": "1+1=", "Answer": 2},
            {"Question": "5+1=", "Answer": 6},
            {"Question": "3+1=", "Answer": 4},
            {"Question": "11+1=", "Answer": 12}
        ]
        return json.dumps(random.choice(Quiz))

    # build dungeon
    def buildDungeon(self):
        roomSettings = {
            "0": "wall",
            "1": "empty",
            "2": "dead end",
            "E": "exit",
            "Q": "quiz",
        }

        # dungeon layout
        dungeon = npy.array(
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
        # print(dungeon)
        return dungeon

    # check if the index in "2D array" is out of range
    def posIsValid(self, xPo, yPo):
        if xPo < 0 or yPo < 0 or xPo >= self.xMax or yPo >= self.yMax:
            return False
        return True

    # check if index is valid
    def isIndexValid(self, xPos, yPos, key, direction):
        d = self.buildDungeon()
        # check if the array index  out of range
        isValid = self.posIsValid(xPos, yPos)
        if isValid == True:
            room = d[xPos][yPos]  # update 4 directions index
            if room != "0":  # if the room is not "Wall"
                self.updateHeadUp(key, direction)
                return key
        return "null"

    # update now position
    def updateNowPos(self, xPos, yPos):
        d = self.buildDungeon()
        nowPosition = d[xPos][yPos]  # update 4 directions index
        self.xPos = xPos
        self.yPos = yPos
        return nowPosition

    # update now position
    # @logger.logPassedRoom
    # def newUpdateNowPos(self, xPos, yPos):
    #     d = self.buildDungeon()
    #     nowPosition = d[xPos][yPos]  # update 4 directions index
    #     self.xPos = xPos
    #     self.yPos = yPos
    #     return nowPosition

    # update head-up
    def updateHeadUp(self, key, direction):
        if self.headUp != "":
            self.headUp += "\n"
        self.headUp += f"Press '{key}' head to {direction}."


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

    # decorator
    # def isIndexValid(self,cb):
    #     xMax = self.xMax
    #     yMax = self.yMax
    #     def checkIndex(xPo, yPo):
    #         if xPo < 0 or yPo < 0 or xPo >= xMax or yPo >= yMax:
    #             return checkIndex
    #         else:cb(xPo, yPo)
    #     return checkIndex

    # update index
    # @isIndexValid
    # def updateIndex(self,xPo,yPo):
    #     d = self.buildDungeon()
    #     return d[xPo][yPo]
