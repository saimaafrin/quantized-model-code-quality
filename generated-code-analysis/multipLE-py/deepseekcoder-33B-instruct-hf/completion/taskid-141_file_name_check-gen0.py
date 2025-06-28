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

    dot_count = 0
    for i in file_name:
        if i == '.':
            dot_count += 1
    if dot_count != 1:
        return 'No'
    else:
        part1, part2 = file_name.split('.')
        if not part1[0].isalpha() or not part1.islower() and not part1.isupper():
            return 'No'
        if not part2 in ['txt', 'exe', 'dll']:
            return 'No'
        digit_count = 0
        for i in part1:
            if i.isdigit():
                digit_count += 1
        if digit_count > 3:
            return 'No'
        return 'Yes'
