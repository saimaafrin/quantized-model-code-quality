def find_most_unhappy_day(schedule) -> int:
    """
    Calculate the day of the week when Jinjin is most unhappy based on her schedule.
    
    Jinjin is unhappy if the total hours spent in school and extra classes exceed 8 hours in a day. 
    The function finds the day when her unhappiness is the greatest, which is the day when the total
    hours are the farthest above the threshold. If there are multiple days with the same level of 
    maximum unhappiness, the earliest day is returned. If Jinjin is not unhappy on any day, the 
    function returns 0.
    
    Args:
        schedule (list[tuple[int, int]]): A list of 7 tuples, where each tuple represents the 
                                           number of hours spent at school and in extra classes
                                           for each day of the week, respectively.
                                           
    Returns:
        int: The day of the week when Jinjin is most unhappy (1-7 for Monday to Sunday) or 0 
             if she is never unhappy.
    
    Cases:
    >>> find_most_unhappy_day([(5, 3), (6, 2), (7, 2), (5, 3), (5, 4), (0, 4), (0, 6)])
    3
    >>> find_most_unhappy_day([(4, 3), (4, 3), (4, 3), (4, 3), (4, 3), (0, 3), (0, 2)])
    0
    """
    days = [sum(day) for day in schedule]
    max_hours = max(days)
    max_unhappy_days = [i + 1 for i, day in enumerate(days) if day == max_hours]
    
    if not max_unhappy_days:
        return 0
    
    return min(max_unhappy_days)
def test_find_most_unhappy_day():
    # Test case 1: Provided example where Jinjin is most unhappy on Wednesday
    schedule1 = [
        (5, 3),
        (6, 2),
        (7, 2),
        (5, 3),
        (5, 4),
        (0, 4),
        (0, 6)
    ]
    assert find_most_unhappy_day(schedule1) == 3, "Test case 1 failed"

    # Test case 2: Jinjin is never unhappy
    schedule2 = [
        (4, 3),
        (4, 3),
        (4, 3),
        (4, 3),
        (4, 3),
        (0, 3),
        (0, 2)
    ]
    assert find_most_unhappy_day(schedule2) == 0, "Test case 2 failed"

    # Test case 3: Jinjin is most unhappy on Monday and Thursday, but Monday should be returned
    schedule3 = [
        (6, 3),
        (6, 2),
        (6, 2),
        (6, 3),
        (6, 2),
        (0, 3),
        (0, 2)
    ]
    assert find_most_unhappy_day(schedule3) == 1, "Test case 3 failed"

    print("All test cases passed.")

# Run the test function
test_find_most_unhappy_day()