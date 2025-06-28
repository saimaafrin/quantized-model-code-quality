def minimum_students_to_leave(heights):
    """
    Calculate the minimum number of students that need to leave to form a choir formation.
    A choir formation is defined such that for some position 'i', the heights of students
    increase from the start to 'i' and decrease from 'i' to the end of the formation.

    Args:
    heights (List[int]): A list of student heights.

    Returns:
    int: The minimum number of students that need to leave.
    """

    def count_increasing(heights):
        """
        Count the number of increasing positions in heights.

        Args:
        heights (List[int]): A list of student heights.

        Returns:
        int: The number of increasing positions.
        """
        count = 0
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                count += 1
        return count

    def count_decreasing(heights):
        """
        Count the number of decreasing positions in heights.

        Args:
        heights (List[int]): A list of student heights.

        Returns:
        int: The number of decreasing positions.
        """
        count = 0
        for i in range(len(heights)-2, 0, -1):
            if heights[i] > heights[i+1]:
                count += 1
        return count

    minimum = len(heights)
    left = 0
    right = len(heights)-1
    while right > left:
        if heights[left] > heights[right]:
            minimum = min(minimum, count_increasing(heights[left:right]))
            right -= 1
        else:
            minimum = min(minimum, count_decreasing(heights[left:right]))
            left += 1
    return minimum
def test_minimum_students_to_leave():
    # Test case 1: Provided example
    assert minimum_students_to_leave([186, 186, 150, 200, 160, 130, 197, 220]) == 4, "Test case 1 failed"

    # Test case 2: All students have the same height
    assert minimum_students_to_leave([150, 150, 150, 150, 150]) == 4, "Test case 2 failed"

    # Test case 3: Students are already in a choir formation
    assert minimum_students_to_leave([130, 150, 170, 190, 170, 150, 130]) == 0, "Test case 3 failed"

    # Test case 4: Students are in strictly increasing order
    assert minimum_students_to_leave([130, 135, 140, 145, 150, 155]) == 0, "Test case 4 failed"

    # Test case 5: Students are in strictly decreasing order
    assert minimum_students_to_leave([155, 150, 145, 140, 135, 130]) == 0, "Test case 5 failed"

    # Test case 6: Optimal choir formation is not including the first or last student
    assert minimum_students_to_leave([200, 180, 190, 170, 210, 160, 220]) == 3, "Test case 6 failed"

    print("All test cases passed!")

# Run the test function
test_minimum_students_to_leave()