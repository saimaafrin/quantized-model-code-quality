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

    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translation = str.maketrans(alphabet, alphabet[26:] + alphabet[:26])

    encoded_message = ''
    for character in message:
        if character in vowels:
            encoded_message += chr(ord(character) + 2)
        elif character in alphabet:
            encoded_message += translation[ord(character)]
        else:
            encoded_message += character
            
    return encoded_message.swapcase()
