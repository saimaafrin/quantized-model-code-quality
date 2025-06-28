def decimal_to_binary(decimal: int) -> str:
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    >>> decimal_to_binary(15)
    'db1111db'
    >>> decimal_to_binary(32)
    'db100000db'
    """

    binary = bin(decimal)[2:]
    binary = binary.replace("0b", "")
    while len(binary) < 10:
        binary = "0" + binary
    binary = "db" + binary + "db"
    return binary
