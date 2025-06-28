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

    # Base case: No fruits to merge
    if len(fruit_counts) == 0:
        return 0

    # Initialize the priority queue with fruits counts as the weights
    min_heap = [(weight, weight) for weight in fruit_counts]
    heapq.heapify(min_heap)

    # Initialize the total cost
    total_cost = 0

    # Merge fruits until only one heap remains
    while len(min_heap) > 1:
        # Pop the smallest heaps from the priority queue
        smallest_heap = heapq.heappop(min_heap)
        smallest_weight = smallest_heap[0]

        # Pop the next smallest heap from the priority queue
        next_smallest_heap = heapq.heappop(min_heap)
        next_smallest_weight = next_smallest_heap[0]

        # Calculate the cost of merging the two heaps
        total_cost += smallest_weight + next_smallest_weight

        # Add the new heap to the priority queue
        heapq.heappush(min_heap, (smallest_weight + next_smallest_weight, smallest_weight + next_smallest_weight))

    # The total cost is the sum of the weights of all fruits in the single heap
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