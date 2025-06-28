from typing import Optional

def string_to_md5(text: str) -> Optional[str]:
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world')
    '3e25960a79dbc69b674cd4ec67a72c62'
    """

    # TODO: Fill out this function to use the md5 library
    # to return the md5 hash of a given string
    # as a string.
    # If the string is empty, return None
    #
    # Remember to handle the case where the text is an empty string
    # by returning None
    #
    # This function should be a one-liner
    #
    # You can import the md5 library using this line of code:
    # from hashlib import md5
    #
    # Then you can calculate the md5 hash using this code:
    # md5(text.encode()).hexdigest()
    return None
