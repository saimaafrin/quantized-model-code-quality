from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    """
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]
    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]
    >>> strange_sort_list([])
    []
    """

    if not lst:
        return lst

    result = []

    while lst:
        min_index = lst.index(min(lst))
        max_index = lst.index(max(lst))

        result.append(lst.pop(max_index))
        if lst:
            result.append(lst.pop(min_index))

    return result
