def valid_date(date: str) -> bool:
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    >>> valid_date('03-11-2000')
    True

    >>> valid_date('15-01-2012')
    False

    >>> valid_date('04-0-2040')
    False

    >>> valid_date('06-04-2020')
    True

    >>> valid_date('06/04/2020')
    False
    """

    days = {1: 31, 3: 31, 5: 30, 7: 31, 8: 31, 10: 30, 12: 31}

    if not date:
        return False

    if '-' not in date:
        return False

    month, day, year = date.split('-')

    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False

    if 1 <= int(month) <= 12:
        pass
    else:
        return False

    if int(month) in days:
        if 1 <= int(day) <= days[int(month)]:
            pass
        else:
            return False

    if int(month) == 2 and 1 <= int(day) <= 28:
        pass
    else:
        return False

    return True
