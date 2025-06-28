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
        return []
    else:
        lst.sort()
        min_num = lst[0]
        max_num = lst[-1]
        result = []
        while lst:
            result.append(min_num)
            lst.remove(min_num)
            if lst:
                max_num = lst[-1]
                result.append(max_num)
                lst.remove(max_num)
                if lst:
                    min_num = lst[0]
        return result
