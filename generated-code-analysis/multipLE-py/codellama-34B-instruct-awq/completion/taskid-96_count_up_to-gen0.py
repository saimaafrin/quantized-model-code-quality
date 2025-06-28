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

    # The list that will be returned
    list_to_be_returned = []

    # This for loop iterates over all the integers below n
    for i in range(2, n):
        # This if statement checks if the current number is a prime number
        if i >= 2:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                list_to_be_returned.append(i)

    return list_to_be_returned
