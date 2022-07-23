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

    # def playerState():
    #     pState = {
    #         "headTo":"where to head menu",
    #         "showLog":"watching log",
    #         "solve":"solve quiz"
    #     }
