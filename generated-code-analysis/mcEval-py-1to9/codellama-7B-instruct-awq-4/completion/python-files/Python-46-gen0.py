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
    # Find the start of the formation.
    start = 0
    while start < len(heights) and heights[start] >= heights[-1]:
        start += 1

    # Find the end of the formation.
    end = len(heights) - 1
    while end >= 0 and heights[end] <= heights[start]:
        end -= 1

    # If the heights were in an increasing order, we don't need to change anything.
    if heights[start] > heights[end]:
        return 0

    # Find the first height that needs to be changed.
    change_height = heights[end]
    for i in range(end, start, -1):
        if heights[i] == change_height:
            continue

        # If the height at position i is less than or equal to the first height
        # that needs to be changed, we don't need to change anything.
        if heights[i] <= change_height:
            break

        # Otherwise, we need to change the height at position i to the first height
        # that needs to be changed.
        heights[i] = change_height
        change_height -= 1

    return len(heights) - end
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