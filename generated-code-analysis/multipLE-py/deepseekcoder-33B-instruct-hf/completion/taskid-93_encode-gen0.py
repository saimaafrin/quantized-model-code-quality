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

    encoded = ''
    for char in message:
        if char.islower():
            if char in 'aeiou':
                char = chr(((ord(char) - ord('a') + 2) % 26) + ord('a'))
                encoded += char.upper()
            else:
                encoded += char.upper()
        else:
            if char in 'AEIOU':
                char = chr(((ord(char) - ord('A') + 2) % 26) + ord('A'))
                encoded += char.lower()
            else:
                encoded += char.lower()
    return encoded
