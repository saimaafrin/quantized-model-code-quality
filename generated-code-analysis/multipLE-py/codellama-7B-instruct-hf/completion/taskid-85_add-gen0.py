from typing import List

def add(lst: List[int]) -> int:
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
    >>> add([4, 2, 6, 7])
    2
    """

    lst = list(map(int, input().split()))
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            sum += lst[i]
    return sum
