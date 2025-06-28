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
    # Initializes the min-heap
    heap = []

    # Initializes the total cost
    total_cost = 0

    # Loops through each fruit type and appends it to the heap
    for fruit in fruit_counts:
        heapq.heappush(heap, fruit)

    # Loops through the heap until only a single heap remains
    while len(heap) > 1:
        # Extracts the two smallest heaps from the heap
        first_heap = heapq.heappop(heap)
        second_heap = heapq.heappop(heap)

        # Calculates the cost of merging the two heaps
        cost = first_heap + second_heap

        # Adds the cost to the total cost
        total_cost += cost

        # Re-adds the merged heap to the heap
        heapq.heappush(heap, cost)

    return total_cost
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