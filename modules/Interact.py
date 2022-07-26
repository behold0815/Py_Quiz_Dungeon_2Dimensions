import os
class Interact:
    def __init__(self):
        pass

    # ask if player wants to play this game
    def askIfWantToPlay(self):
        while True:
            yesOrNo = input("Do you want to play Quiz Dungeon? (y)es/(n)o:")

            if yesOrNo != "y" and yesOrNo != "n":
                print("Please enter y for 'Yes' or n for 'No'.")
                continue
            elif yesOrNo == "n":
                quit()
            else:
                break  # yes

    def welcomeWords(self):
        words = """
        ==================================================================
        § Welcome to Quiz Dungeon!!
        § You can press 'Ctrl + C' to Exit Dungeon anytime.
        § Press any key when you are ready to start the adventure!!!
        ==================================================================
        """
        print(words)
        os.system("pause")
        print("You've entered Quiz Dungeon.")

    # display result
    def disPlay(self,*args):
        os.system("cls")
        print(args[0]) # heads up
        args[1]() # execute def
        os.system("pause")
    # def playerState():
    #     pState = {
    #         "headTo":"where to head menu",
    #         "showLog":"watching log",
    #         "solve":"solve quiz"
    #     }
