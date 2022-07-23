import datetime


class dateTimeFormat:
    def __init__(self):
        self.getToday = datetime.datetime.today()

    def getDateTime(self):
        loc_dt_format = self.getToday.strftime("%Y/%m/%d %H:%M:%S")
        return loc_dt_format

    def getDate(self):
        loc_dt_format = self.getToday.strftime("%Y/%m/%d")
        return loc_dt_format

# t = dateTimeFormat()
# print(t.getDateTime())
