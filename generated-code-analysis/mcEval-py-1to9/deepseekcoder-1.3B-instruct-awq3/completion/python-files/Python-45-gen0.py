import heapq
from typing import List 

def minimum_cost_to_merge_fruits(fruit_counts: List[int]) -> int:
    """
    Calculates the minimum total cost to merge multiple heaps of fruits into a single heap.
    The cost of merging two heaps is equal to the sum of their weights. The function utilizes
    a greedy algorithm with a min-heap (priority queue) to ensure the smallest heaps are merged first,
    minimizing the total cost.

    Parameters:
    fruit_counts (List[int]): A list of integers representing the counts of each type of fruit.

    Returns:
    int: The minimum total cost required to merge all heaps of fruits.

    Examples:
    >>> minimum_cost_to_merge_fruits([1, 2, 9])
    15
    >>> minimum_cost_to_merge_fruits([10, 20, 30, 40, 50])
    300 .
    """

    # Convert fruit_counts list to a min-heap
    heapq.heapify(fruit_counts)

    total_cost = 0

    while len(fruit_counts) > 1:
        # Merge two smallest fruits and add its cost to total cost
        total_cost += -heapq.heappop(fruit_counts) + -heapq.heappop(fruit
        t

    return total_cost


print(minimum_cost_to_merge_fruits([1, 2, 9]))
print(minimum_cost_to_merge_fruits([10, 20, 30, 40, 50]))
print(minimum_cost_to_merge_fruits([1, 3, 1, 5, 3, 5, 7]))
print(minimum_cost_to_merge_fruits([1, 1, 1, 1, 1, 1, 1]))
print(minimum_cost_to_merge_fruits([1, 2, 3, 4, 5]))
print(minimum_cost_to_merge_fruits([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(minimum_cost_to_merge_fruits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(minimum_cost_to_merge_fruits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(minimum_cost_to_merge_fruits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
print(minimum_cost_to_merge_fruits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(minimum_cost_to_merge_fruits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
print(minimum_cost_to_merge_fruits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
print(minimum_cost_to_merge_fruits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
print(minimum_cost_to_merge
def test_minimum_cost_to_merge_fruits():
    # Test case 1: As provided in the problem statement example
    fruits1 = [1, 2, 9]
    assert minimum_cost_to_merge_fruits(fruits1) == 15, "Test case 1 failed"

    # Test case 2: Simple case with only two types of fruits
    fruits2 = [5, 5]
    assert minimum_cost_to_merge_fruits(fruits2) == 10, "Test case 2 failed"

    # Test case 3: More complex case with multiple types of fruits
    fruits3 = [10, 20, 30, 40, 50]
    assert minimum_cost_to_merge_fruits(fruits3) == 330, "Test case 3 failed"

    # Test case 4: Case with fruits having the same count
    fruits4 = [3, 3, 3, 3]
    assert minimum_cost_to_merge_fruits(fruits4) == 24, "Test case 4 failed"

    # Test case 5: Case with a single type of fruit
    fruits5 = [7]
    assert minimum_cost_to_merge_fruits(fruits5) == 0, "Test case 5 failed"

    print("All test cases passed.")

# Run the test function
test_minimum_cost_to_merge_fruits()