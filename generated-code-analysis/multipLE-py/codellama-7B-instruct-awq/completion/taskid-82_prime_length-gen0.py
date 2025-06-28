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

    # Write your code here
    if len(string) == 0:
        return False
    if len(string) == 1:
        return False
    for i in range(2, len(string)):
        if len(string) % i == 0:
            continue
        else:
            return False
    return True
