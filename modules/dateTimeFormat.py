import datetime


class dateTimeFormat:
    def __init__(self): pass

    def getDateTime(self):
        loc_dt = datetime.datetime.today()
        loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
        return loc_dt_format

# t = dateTimeFormat()
# print(t.getDateTime())
