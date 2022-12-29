import datetime
import holidays


def isHoliday(today=datetime.datetime.today()):
    return any(x for x in holidays.Czechia(years=[today.year]) if today.date() == x)
