def check_scenario(scenario: str, liar_count: set, statements: dict, days_of_week: set) -> bool:
    """
    Evaluates the consistency of a scenario where one participant is the criminal based on the given statements.

    This function takes a potential criminal's name (scenario) and a set of liars (liar_count) and checks if
    the statements made by all participants are consistent with this scenario, disregarding any statements
    about the day of the week.

    Parameters:
    - scenario (str): The name of the participant being tested as the potential criminal.
    - liar_count (set): A set of names of participants who are assumed to be liars.
    - statements (dict): A dictionary mapping participant names to lists of their respective statements.
    - days_of_week (set): A set of strings representing the days of the week.

    Returns:
    - bool: True if the scenario is consistent with the statements, False otherwise.

    Test Cases:
    >>> check_scenario("ALICE", {"BOB", "CHARLIE"}, {"ALICE": ["I am guilty."], "BOB": ["ALICE is not guilty."], "CHARLIE": []}, {"MONDAY", "TUESDAY"})
    True
    """
    # Check if any statement directly contradicts the scenario
    for person, statements_list in statements.items():
        for statement in statements_list:
            if (statement == "I am guilty." and person != scenario) or (
                statement == "I am not guilty." and person == scenario
            ):
                return False

    # Check if any pair of participants are consistent with each other
    for person1, statements_list1 in statements.items():
        for person2, statements_list2 in statements.items():
            # Don't check if person1 and person2 are the same person
            if person1 == person2:
                continue
            # Don't check if person1 and person2 are consistent with the scenario
            if (
                (person1 == scenario and "I am guilty." not in statements_list2)
                or (person2 == scenario and "I am guilty." not in statements_list1)
                or (
                    person1 != scenario
                    and person2 != scenario
                    and "I am not guilty." not in statements_list1
                    and "I am not guilty." not in statements_list2
                )
            ):
                continue
            # Check if person1 and person2 are both liars
            if person1 in liar_count and person2 in liar_count:
                # Both liars should be consistent with each other
                for statement1 in statements_list1:
                    if statement1 not in statements_list2:
                        return False
            # Check if only person1 is a liar
            elif person1 in liar_count:
                # Person1 should be inconsistent with person2
                for statement1 in statements_list1:
                    if statement1 in statements_list2:
                        return False
            # Check if only person2 is a liar
            elif person2 in liar_count:
                # Person2 should be inconsistent with person1
                for statement2 in statements_list2:
                    if statement2 in statements_list1:
                        return False
            # Check if neither person1 nor person2 are liars
            else:
                # Both participants should be consistent with each other
                for statement1 in statements_list1:
                    if statement1 not in statements_list2:
                        return False

    # Check if any statement mentions the day of the week and evaluate its consistency with the scenario
    for person, statements_list in statements.items():
        for statement in statements_list:
            if statement in days_of_week and person == scenario:
                return False
            if statement in days_of_week and person != scenario:
                return True

    return True
def test_check_scenario():
    # Define a set of days of the week for the test cases
    days_of_week = set(["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"])

    # Test case 1: Simple case where the scenario is correct
    statements_test1 = {
        "ALICE": ["I am not guilty.", "BOB is guilty."],
        "BOB": ["ALICE is not guilty.", "Today is MONDAY"],
        "CHARLIE": ["I am guilty."]
    }
    scenario_test1 = "CHARLIE"
    liar_count_test1 = {"ALICE", "BOB"}
    assert check_scenario(scenario_test1, liar_count_test1, statements_test1, days_of_week) == False, "Test case 1 failed"

    # Test case 2: Scenario with contradictory statements
    statements_test2 = {
        "ALICE": ["I am guilty."],
        "BOB": ["I am not guilty.", "ALICE is guilty."],
        "CHARLIE": ["I am not guilty.", "Today is TUESDAY"]
    }
    scenario_test2 = "ALICE"
    liar_count_test2 = {"BOB", "CHARLIE"}
    assert check_scenario(scenario_test2, liar_count_test2, statements_test2, days_of_week) == False, "Test case 2 failed"

    # Test case 3: Scenario where the statements are ambiguous
    statements_test3 = {
        "ALICE": ["I am not guilty.", "Today is WEDNESDAY"],
        "BOB": ["I am not guilty.", "CHARLIE is guilty."],
        "CHARLIE": ["BOB is not guilty."]
    }
    scenario_test3 = "BOB"
    liar_count_test3 = {"ALICE", "CHARLIE"}
    assert check_scenario(scenario_test3, liar_count_test3, statements_test3, days_of_week) == False, "Test case 3 failed"

    print("All test cases passed.")

# Run the test function
test_check_scenario()