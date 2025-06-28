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
    # if there is only one student in the choir, no one needs to leave.
    if len(heights) == 1:
        return 0

    # number of students that need to leave.
    students_to_leave = 0

    # the current number of students to the left of the choir formation.
    left = 0

    # the current number of students to the right of the choir formation.
    right = len(heights) - 1

    # the height of the left-most student.
    left_height = heights[left]

    # the height of the right-most student.
    right_height = heights[right]

    # the height of the student currently in the choir formation.
    current_height = 0

    # iterate through the students.
    while left_height < right_height:
        # if the left height is less than the right height.
        if left_height < right_height:
            # update the current height to be the left height.
            current_height = left_height

            # increment the number of students to leave.
            students_to_leave += 1

            # move the left to the right.
            left += 1

            # update the left height.
            left_height = heights[left]
        else:
            # update the current height to be the right height.
            current_height = right_height

            # increment the number of students to leave.
            students_to_leave += 1

            # move the right to the left.
            right -= 1

            # update the right height.
            right_height = heights[right]

    return students_to_leave
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