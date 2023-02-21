
def yearLength(year):
    if year % 400 == 0:
        return 366
    elif year % 100 == 0:
        return 365
    elif year % 4 == 0:
        return 366
    else:
        return 365

def monthLength(year, month):
    if month == 2 and yearLength(year) == 366:
        return 29
    elif month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def dateDays(year, month, day):
    yeardays = 0
    for y in range(year):
        yeardays = yeardays + yearLength(y)
    monthdays = 0
    for m in range(1, month):
        monthdays = monthdays + monthLength(year, m)
    days = yeardays + monthdays + day
    return days



def dateDiff(year1, month1, day1, year2, month2, day2):
    diff = ( dateDays(year2, month2, day2)        
           - dateDays(year1, month1, day1))
    return diff


def main():
    year1, month1, day1 = eval(input('start date: '))
    year2, month2, day2 = eval(input('end date: '))
    diff = dateDiff(year1, month1, day1, year2, month2, day2)
    print('result', diff, 'days')

if __name__ == '__main__':
    main()

