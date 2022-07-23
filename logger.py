
from modules.dateTimeFormat import dateTimeFormat

class logger(object):
    def __init__(self):
        dT = dateTimeFormat()
        self.Date = dT.getDate().replace("/", "")  # yyyyMMdd

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs) # if method return anything, you must use return
            dT = dateTimeFormat()
            with open(f"{self.Date}_log.txt", "a", encoding='utf-8') as f:
                f.write(f"{dT.getDateTime()} You move to position {args[0].xPos,args[0].yPos,}\n")
            return result # if method return anything, you must use return
        return wrapper

    def showLog(self):
        with open(f"{self.Date}_log.txt","r") as f:
            print(f.read())


