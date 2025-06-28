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

    # Initialize a dictionary to store the total height at each position
    total_height = {0: 0}
    for i in range(1, len(heights)):
        total_height[i] = heights[i - 1] + total_height[i - 1]

    # Find the max height index
    max_height_index = len(heights) - 1
    while max_height_index > 0 and heights[max_height_index - 1] > heights[max_height_index]:
        max_height_index -= 1

    # Calculate the number of students that need to leave
    num_to_leave = 0
    for i in range(max_height_index, 0, -1):
        # If the total height is greater than or equal to the starting height,
        # the student needs to leave and contribute to the total height
        if total_height[i] >= heights[i - 1]:
            num_to_leave += 1
        else:
            break

    return num_to_leave
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