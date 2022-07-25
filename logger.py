from modules.dateTimeFormat import dateTimeFormat

class logger(object):
    def __init__(self,func):
        dT = dateTimeFormat()
        self.Date = dT.getDate().replace("/", "")  # yyyyMMdd
        self.f = func

    def __call__(self, *args, **kwargs):
        result = self.f(*args, **kwargs) # if method return anything, you must use return
        dT = dateTimeFormat()
        with open(f"{self.Date}_log.txt", "a", encoding='utf-8') as f:
            f.write(f"{dT.getDateTime()} You move to position {args[1],args[2]}\n")
        return result # if method return anything, you must use return




