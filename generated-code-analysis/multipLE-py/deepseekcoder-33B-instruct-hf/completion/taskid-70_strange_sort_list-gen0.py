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
    min_val = min(lst)
    max_val = max(lst)
    min_count = lst.count(min_val)
    max_count = lst.count(max_val)
    min_lst = [min_val] * min_count
    max_lst = [max_val] * max_count
    remaining = [i for i in lst if i != min_val and i != max_val]
    if len(lst) % 2 == 0:
        # if length of list is even, we need to add min_val at start and max_val at end
        return min_lst + strange_sort_list(remaining) + max_lst
    else:
        # if length of list is odd, we need to add max_val at start and min_val at end
        return max_lst + strange_sort_list(remaining) + min_lst
