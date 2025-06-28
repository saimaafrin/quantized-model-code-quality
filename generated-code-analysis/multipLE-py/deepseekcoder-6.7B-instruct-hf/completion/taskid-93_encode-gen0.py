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

    vowels = 'aeiou'
    encoded = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded += chr(ord(char) + 2) if char.islower() else chr(ord(char) + 2).upper()
            else:
                encoded += char.upper() if char.islower() else char.lower()
        else:
            encoded += char
    return encoded
