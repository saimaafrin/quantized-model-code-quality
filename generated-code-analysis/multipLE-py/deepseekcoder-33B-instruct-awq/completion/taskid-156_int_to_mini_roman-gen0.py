def int_to_mini_roman(number: int) -> str:
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19)
    'xix'
    >>> int_to_mini_roman(152)
    'clii'
    >>> int_to_mini_roman(426)
    'cdxxvi'
    """

    roman_nums = ['i', 'v', 'x', 'l', 'c', 'd']
    values = [1, 5, 10, 50, 100, 500]
    num_str = str(number)
    output = ''
    for num in num_str:
        index = num_str.index(num)
        if index == 3:
            output += 'm' * int(num)
        else:
            current = values[index * 2 - 2]
            next_ = values[index * 2 - 1]
            if int(num) < 4:
                output += roman_nums[index * 2 - 2] * int(num)
            elif int(num) == 4:
                output += roman_nums[index * 2 - 2] + roman_nums[index * 2 - 1]
            elif int(num) < 9:
                output += roman_nums[index * 2 - 1] + roman_nums[index * 2 - 2] * (int(num) - 5)
            else:
                output += roman_nums[index * 2 - 2] + roman_nums[index * 2]
    return output
