from typing import List

def count_up_to(n: int) -> List[int]:
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    >>> count_up_to(5)
    [2, 3]
    >>> count_up_to(11)
    [2, 3, 5, 7]
    >>> count_up_to(0)
    []
    >>> count_up_to(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> count_up_to(1)
    []
    >>> count_up_to(18)
    [2, 3, 5, 7, 11, 13, 17]
    """


    # TODO: Implement count_up_to
    result = []
    for i in range(2, n+1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            result.append(i)

    return result
