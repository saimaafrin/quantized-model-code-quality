def file_name_check(file_name: str) -> str:
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    >>> file_name_check('example.txt')
    'Yes'
    >>> file_name_check('1example.dll')
    'No'
    """

    import re

    # Match file name format
    # ^ - start of string
    # [a-zA-Z] - first character should be a letter
    # [a-zA-Z0-9]{0,2} - next characters can be letters or digits, up to 2 of them
    # \. - should be a dot
    # [a-zA-Z]{1,3}$ - should be one or more letters at the end of the string
    match = re.fullmatch(r"^[a-zA-Z]{1,2}\d{0,3}\.[a-z]{3}$", file_name.split('.')[0])
    
    return 'Yes' if match else 'No'
