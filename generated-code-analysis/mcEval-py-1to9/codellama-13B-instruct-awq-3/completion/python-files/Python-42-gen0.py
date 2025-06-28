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
    # 1. initialize variables to track the total hours in school and extra classes
    total_hours_in_school = [0] * 7
    total_hours_in_extra_classes = [0] * 7
    
    # 2. calculate the total hours in school and extra classes for each day of the week
    for day in range(len(schedule)):
        total_hours_in_school[day] = schedule[day][0]
        total_hours_in_extra_classes[day] = schedule[day][1]
        
    # 3. calculate the total unhappiness for each day of the week
    total_unhappiness = [0] * 7
    for day in range(len(schedule)):
        total_unhappiness[day] = total_hours_in_school[day] + total_hours_in_extra_classes[day]
        
    # 4. find the day when Jinjin is most unhappy
    index_of_most_unhappy_day = total_unhappiness.index(max(total_unhappiness))
    
    # 5. if Jinjin is not unhappy on any day, return 0
    if max(total_unhappiness) <= 8:
        index_of_most_unhappy_day = 0
    
    # 6. return the day of the week when Jinjin is most unhappy (1-7 for Monday to Sunday)
    return index_of_most_unhappy_day + 1
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