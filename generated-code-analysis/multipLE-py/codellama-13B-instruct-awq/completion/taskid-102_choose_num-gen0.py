def choose_num(x: int, y: int) -> int:
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    >>> choose_num(12, 15)
    14
    >>> choose_num(13, 12)
    -1
    """


    if x > y:
        raise ValueError("The first argument must be less than or equal to the second argument")

    # Check if there are any even numbers in the range
    if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
        return -1

    # Check if x is odd
    if x % 2 != 0:
        # Check if x is in the range
        if x <= y:
            # Check if y is in the range
            if y <= 2*x:
                return 2*x
            else:
                # Check if the even number is in the range
                for i in range(2*x, y+1, 2):
                    if i <= y:
                        return i
                    else:
                        return -1
        else:
            return -1

    # Check if x is even
    if x % 2 == 0:
        # Check if y is in the range
        if y <= 2*x:
            return 2*x
        else:
            # Check if the even number is in the range
            for i in range(2*x, y+1, 2):
                if i <= y:
                    return i
                else:
                    return -1

    return -1
