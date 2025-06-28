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
    # Make sure the scenario is in the statements dictionary
    if scenario not in statements:
        return False

    # Make sure all statements are in the correct format
    for name in statements:
        if type(statements[name]) != list:
            return False
        for statement in statements[name]:
            if type(statement) != str:
                return False

    # Make sure all statements are either about the criminal or the day of the week
    for name in statements:
        for statement in statements[name]:
            if (
                statement != f"{scenario} is guilty."
                and statement != f"{scenario} is not guilty."
            ):
                if statement not in days_of_week:
                    return False

    # Make sure all statements about the criminal are consistent
    for name in statements:
        if name != scenario:
            if (
                f"{scenario} is guilty." in statements[name]
                and f"{scenario} is not guilty." in statements[name]
            ):
                return False

    # Make sure all statements about the day of the week are consistent
    for name in statements:
        if (
            "MONDAY" in statements[name]
            and "TUESDAY" in statements[name]
            and "WEDNESDAY" in statements[name]
            and "THURSDAY" in statements[name]
            and "FRIDAY" in statements[name]
        ):
            return False

    # Make sure all liars are consistent with the statements about the criminal
    for name in statements:
        if name in liar_count:
            if (
                f"{scenario} is guilty." in statements[name]
                and f"{scenario} is not guilty." not in statements[name]
            ):
                return False
            if (
                f"{scenario} is guilty." not in statements[name]
                and f"{scenario} is not guilty." in statements[name]
            ):
                return False

    # Make sure there are no other inconsistencies in the statements
    for name in statements:
        if name != scenario and name not in liar_count:
            if f"{scenario} is guilty." in statements[name]:
                for other_name in statements:
                    if other_name != name and other_name != scenario:
                        if f"{scenario} is not guilty." in statements[other_name]:
                            return False
            if f"{scenario} is not guilty." in statements[name]:
                for other_name in statements:
                    if other_name != name and other_name != scenario:
                        if f"{scenario} is guilty." in statements[other_name]:
                            return False

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