from modules.dateTimeFormat import dateTimeFormat

dT = dateTimeFormat()
Date = dT.getDate().replace("/", "")  # yyyyMMdd
Dtime = dT.getDateTime()

class logger:

    # write log into file
    def writeLog(func):
        def wra(*args, **kwargs):
            r = func(*args, **kwargs)
            with open(f"{Date}_log.txt", "a", encoding='utf-8') as f:
                f.write(
                    f"{Dtime} You move to position {args[1],args[2]}\n")
            return r
        return wra

    # show log
    def showLog():
        try:
            with open(f"{Date}_log.txt", "r") as f:
                print(f.read())
        except OSError as e:
            print("No such file or directory.")





