def prime_length(string: str) -> bool:
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    >>> prime_length('Hello')
    True
    >>> prime_length('abcdcba')
    True
    >>> prime_length('kittens')
    True
    >>> prime_length('orange')
    False
    """

    # Calculate the length of the string
    string_length = len(string)

    # If the string length is less than 2, it is not a prime
    if string_length < 2:
        return False

    # Check each number up to the square root of the string length
    for num in range(2, int(string_length**0.5) + 1):
        # If the string length is divisible by any number up to the square root,
        # it is not a prime
        if string_length % num == 0:
            return False

    # If none of the numbers divide the string length, it is a prime
    return True
