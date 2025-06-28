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
    # 1. If there are less than 4 students, then there is no choir formation
    # possible, so we can return early.
    if len(heights) < 4:
        return 0

    # 2. Sort the list of heights in ascending order.
    sorted_heights = sorted(heights)

    # 3. Iterate over each student in the sorted list, and count the number
    # of students that are higher than them.
    # We can do this by iterating over each height in the sorted list, and
    # comparing it to every other height in the sorted list.
    count = 0
    for height in sorted_heights:
        # We need to count the number of students that are higher than the
        # current height. To do this, we can iterate over every height in
        # the sorted list, and check if it is greater than the current
        # height. If it is, then we can increment the count.
        # However, we don't need to compare the current height to itself, so
        # we can skip over that height in the sorted list.
        for other_height in sorted_heights[1:]:
            if other_height > height:
                count += 1

    # 4. Return the minimum number of students that need to leave.
    return count
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