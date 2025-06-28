def get_max_triples(n: int) -> int:
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
    >>> get_max_triples(5)
    1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

    def gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x

    def lcm(x: int, y: int) -> int:
        return x * y // gcd(x, y)

    def count_divisible_by(x: int, y: int) -> int:
        return x // y

    count = [0] * 3
    a = []
    for i in range(1, n+1):
        a.append(i*i - i + 1)
        count[a[-1] % 3] += 1

    total = count_divisible_by(count[0], 3)
    for i in range(1, 3):
        for j in range(i+1, 3):
            total += count_divisible_by(count[i] * count[j], 6 // gcd(3, 6 - 3 * i - 3 * j))

    return total
