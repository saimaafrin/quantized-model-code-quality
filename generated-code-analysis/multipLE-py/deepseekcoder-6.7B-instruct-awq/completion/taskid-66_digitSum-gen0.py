def digitSum(s: str) -> int:
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
    >>> digitSum('')
    0
    >>> digitSum('abAB')
    131
    >>> digitSum('abcCd')
    67
    >>> digitSum('helloE')
    69
    >>> digitSum('woArBld')
    131
    >>> digitSum('aAaaaXa')
    153
    """


    # Convert string to list of characters
    chars = list(s)

    # Initialize sum
    sum = 0

    # Iterate through the list of characters
    for c in chars:
        # If the character is an uppercase letter
        if c.isupper():
            # Add its ASCII value to the sum
            sum += ord(c)

    # Return the sum
    return sum
