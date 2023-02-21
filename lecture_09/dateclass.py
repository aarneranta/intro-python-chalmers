def year_length(year):
    if year % 400 == 0:
        return 366
    elif year % 100 == 0:
        return 365
    elif year % 4 == 0:
        return 366
    else:
        return 365


def month_length(year, month):
    if month == 2 and year_length(year) == 366:
        return 29
    elif month == 2:
        return 28
    elif month in [4,6,9,11]:
        return 30
    else:
        return 31



class Date:

    def __init__(self, year, month, day):
        if (0 < month <= 12) and (0 < day <= month_length(year, month)):
            self.year = year
            self.month = month
            self.day = day

    def date_days(self):
        days = 0
        for y in range(self.year):
            days = days + year_length(y)
        for m in range(1, self.month):
            days = days + month_length(self.year, m)
        return days + self.day


def date_diff(date1, date2):
    return date_days(date2) - date_days(date1)


      
