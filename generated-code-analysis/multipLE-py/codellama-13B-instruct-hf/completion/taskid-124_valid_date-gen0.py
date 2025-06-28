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

    # Check if the date is not empty
    if date == "":
        return False

    # Check if the date is in the format: mm-dd-yyyy
    if date.count("-") != 2 or date.count("-") != 1:
        return False

    # Check if the date has 3 elements
    if len(date.split("-")) != 3:
        return False

    # Check if the first element is a number
    if not date.split("-")[0].isnumeric():
        return False

    # Check if the second element is a number
    if not date.split("-")[1].isnumeric():
        return False

    # Check if the third element is a number
    if not date.split("-")[2].isnumeric():
        return False

    # Check if the number of days is correct
    days_month = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    month = int(date.split("-")[0])
    days = int(date.split("-")[1])
    if month not in days_month:
        return False
    if days < 1 or days > days_month[month]:
        return False

    # Check if the month is correct
    month = int(date.split("-")[0])
    if month < 1 or month > 12:
        return False

    # Check if the year is correct
    year = int(date.split("-")[2])
    if year < 1970 or year > 2021:
        return False

    return True
