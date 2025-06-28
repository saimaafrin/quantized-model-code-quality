def encode(message: str) -> str:
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """

    vowels = "aeiou"
    message = list(message)
    for i in range(len(message)):
        if message[i].isupper():
            message[i] = message[i].lower()
        elif message[i].islower():
            message[i] = message[i].upper()
        if message[i] in vowels:
            index = vowels.index(message[i])
            message[i] = vowels[(index + 2) % 5]
    return "".join(message)
