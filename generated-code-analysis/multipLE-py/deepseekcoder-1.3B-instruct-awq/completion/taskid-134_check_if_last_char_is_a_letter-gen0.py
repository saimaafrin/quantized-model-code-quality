def check_if_last_char_is_a_letter(txt: str) -> bool:
    """
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    >>> check_if_last_char_is_a_letter('apple pie')
    False
    >>> check_if_last_char_is_a_letter('apple pi e')
    True
    >>> check_if_last_char_is_a_letter('apple pi e ')
    False
    >>> check_if_last_char_is_a_letter('')
    False
    """


    # Split the string into words
    words = txt.split()

    # If the string is empty or there are no words
    if not words or len(words) == 0:
        return False

    # Get the last word and its last character
    last_word = words[-1]
    last_char = last_word[-1]

    # Check if the last character is an alphabet and not part of a word
    if not last_char.isalpha() or last_char in 'aeiouAEIOU':
        return False

    return True
