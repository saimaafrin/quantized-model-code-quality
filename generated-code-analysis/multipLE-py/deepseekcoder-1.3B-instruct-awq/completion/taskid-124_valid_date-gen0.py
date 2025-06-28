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

    import re

    date_pattern = re.compile(r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-[0-9]{4}$")
    date_parts = date.split("-")

    if len(date_parts) != 3:
        return False

    month, day, year = map(int, date_parts)

    if month < 1 or month > 12 or day < 1 or year < 1:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False

    if month == 2 and day > 29:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if not date_pattern.match(date):
        return False

    return True
