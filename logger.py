from modules.dateTimeFormat import dateTimeFormat
log = []
DTF = dateTimeFormat()
T = DTF.getDateTime()

class logger:
    def writeLog(self, words):
        log.append(f"{T}_{words}")

    def showLog(self):
        for s in log:
            print(s)

# logObj = logger()
# logObj.writeLog("test4")
# logObj.showLog()


