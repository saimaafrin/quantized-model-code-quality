from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """


    numbers.sort()

    last = None
    result = []

    for n in numbers:
        if last is None or n != last:
            result.append(n)
            last = n

    return result
\end{code}
