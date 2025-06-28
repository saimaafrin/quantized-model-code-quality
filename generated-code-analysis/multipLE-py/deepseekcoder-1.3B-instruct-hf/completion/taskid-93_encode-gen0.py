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

    def shift_vowel(char: str) -> str:
        vowels = "aeiou"
        if char.lower() in vowels:
            index = vowels.index(char.lower())
            if char.isupper():
                return chr((index + 2) % 26 + 65)
            else:
                return chr((index + 2) % 26 + 97)
        else:
            return char

    return "".join(map(shift_vowel, message))
