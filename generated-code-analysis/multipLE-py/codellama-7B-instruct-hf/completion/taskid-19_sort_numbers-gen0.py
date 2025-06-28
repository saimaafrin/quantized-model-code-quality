def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # split the input into a list of single number strings
    nums = numbers.split()
    # sort the list using a custom key that returns the numeric value of each number
    nums.sort(key=lambda x: str_to_num(x))
    # convert back to a string
    return ' '.join(nums)
