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

    vowels = 'AEIOUaeiou'
    result = []

    for char in message:
        if char in vowels:
            index = vowels.index(char)
            result.append(vowels[(index + 2) % len(vowels)])
        elif char.isalpha():
            if char.isupper():
                result.append(char.lower())
            else:
                result.append(char.upper())
        else:
            result.append(char)

    return ''.join(result)
