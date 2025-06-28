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

    # First, validate input.
    if not heights:
        return 0

    # Initialize a stack.
    stack = []

    # Iterate through the heights, keeping track of the largest and smallest
    # heights seen so far.
    current_min = heights[0]
    current_max = heights[0]
    for height in heights:
        if height > current_max:
            current_max = height
        elif height < current_min:
            current_min = height

        # If the current height is a local maximum, the students above it can
        # now be removed.
        if height == current_max:

            # Remove students above the current maximum.
            while stack and stack[-1] > current_max:
                stack.pop()

            # Push the current maximum onto the stack.
            stack.append(current_max)

            # Reset the minimum height.
            current_min = current_max

            # Reset the maximum height.
            current_max = height

    # Calculate the number of students that need to leave.
    return len(heights) - len(stack)
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