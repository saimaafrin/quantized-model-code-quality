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

    encoded_message = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                # If c is uppercase, make it lowercase, 
                # and then use the lowercase equivalent of 
                # the letter that is 2 places ahead of it
                encoded_message += chr(ord(c.lower()) + 2)
            else:
                # If c is lowercase, make it uppercase, 
                # and then use the uppercase equivalent of 
                # the letter that is 2 places ahead of it
                encoded_message += chr(ord(c.upper()) + 2)
        else:
            # If the character isn't a letter, just add it to the encoded message
            encoded_message += c
    return encoded_message
