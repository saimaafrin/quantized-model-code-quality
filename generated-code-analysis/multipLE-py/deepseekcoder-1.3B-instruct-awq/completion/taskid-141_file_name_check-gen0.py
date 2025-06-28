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


    def check_one_digit(file_name: str) -> bool:
        return len(file_name) <= 3 and not file_name.isdigit()

    def check_dot(file_name: str) -> bool:
        return file_name.count('.') == 1

    def check_substr(file_name: str) -> bool:
        substrs = file_name.split('.')
        return substrs[0] and substrs[0][0].isalpha() and substrs[0][1:].isalpha() and substrs[1] in ['txt', 'exe', 'dll']

    return 'Yes' if all([check_one_digit(file_name), check_dot(file_name), check_substr(file_name)]) else 'No'
