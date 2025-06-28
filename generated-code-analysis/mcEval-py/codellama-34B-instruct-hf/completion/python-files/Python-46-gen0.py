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

    # The maximum number of students that can leave and still have a valid choir
    # formation is equal to the number of students in the list divided by 2.
    max_students_to_leave = len(heights) // 2

    # The minimum number of students that can leave is 0.
    min_students_to_leave = 0

    # Loop through the possible number of students to leave and check if a valid
    # choir formation exists. If it does, update the minimum number of students
    # to leave and the maximum number of students to leave.
    for students_to_leave in range(max_students_to_leave, min_students_to_leave - 1, -1):
        # If a valid choir formation exists, update the minimum number of students
        # to leave and the maximum number of students to leave.
        if choir_formation_exists(heights, students_to_leave):
            min_students_to_leave = students_to_leave
            break

    return min_students_to_leave
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