from typing import List

def unique_digits(x: List[int]) -> List[int]:
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    res = []
    for i in x:
        if str(i).count("0") == 0 and str(i).count("2") == 0 and str(i).count("4") == 0 and str(i).count("6") == 0 and str(i).count("8") == 0:
            res.append(i)
    return sorted(res)
