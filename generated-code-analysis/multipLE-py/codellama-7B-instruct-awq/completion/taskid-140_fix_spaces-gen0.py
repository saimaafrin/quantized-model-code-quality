def fix_spaces(text: str) -> str:
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    >>> fix_spaces(' Example')
    'Example'
    >>> fix_spaces(' Example 1')
    'Example_1'
    >>> fix_spaces(' Example 2')
    '_Example_2'
    >>> fix_spaces(' Example 3')
    '_Example-3'
    """

    # Write your code here
    count = 0
    res = []
    for i in range(len(text)):
        if text[i] != " ":
            res.append(text[i])
        elif text[i] == " " and count == 0:
            res.append("_")
            count += 1
        elif text[i] == " " and count > 0:
            res.append("-")
            count += 1

    return "".join(res)
