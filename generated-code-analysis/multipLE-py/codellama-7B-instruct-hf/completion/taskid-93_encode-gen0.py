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

    # Your code here
    message_to_list = list(message)
    message_to_list_swapped = []
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(message_to_list)):
        if message_to_list[i].islower():
            message_to_list_swapped.append(message_to_list[i].upper())
        else:
            message_to_list_swapped.append(message_to_list[i].lower())
    for i in range(len(message_to_list)):
        if message_to_list[i] in vowels:
            if i + 2 < len(message_to_list):
                message_to_list_swapped[i] = message_to_list_swapped[i + 2]
    encoded = "".join(message_to_list_swapped)
    return encoded
