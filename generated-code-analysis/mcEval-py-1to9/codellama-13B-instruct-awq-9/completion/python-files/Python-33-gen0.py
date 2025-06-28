def calculate_score(system: int, points: str) -> list:
    """
    Calculate the score of a series of ping-pong games based on the provided scoring system.

    This function takes in the desired scoring system (either 11 or 21 points) and a string 
    representing the sequence of points won by the player ('W') and the opponent ('L'). 
    The function processes the string and returns a list of game scores formatted as "player_score:opponent_score".

    The game is considered finished when one player reaches the system's required number of points 
    (11 or 21) with at least a 2-point lead. If the sequence of points ends in the middle of a game, 
    that game's current score is also included in the output.

    Args:
    - system (int): The number of points required to win a game (either 11 or 21).
    - points (str): A string of 'W' and 'L' characters denoting points won by the player and opponent.

    Returns:
    - list: A list of strings representing the score of each game.

    Cases:
    >>> calculate_score(11, "WWWWWWWWWWL")
    ["10:1"]
    """
    score = 0
    games = []
    current_game = []
    last_points_won = ""

    for point in points:
        if point == "W":
            score += 1
        else:
            score -= 1

        current_game.append(point)
        if (point == "W" and score == system - 1) or (point == "L" and score == -1):
            # score is tied
            games.append(f"{score}:{score}")
        elif point == "W" and score == system:
            # player wins
            games.append(f"{score - 1}:0")
        elif point == "L" and score == -system:
            # opponent wins
            games.append(f"0:{score + 1}")
        elif point == "W" and score == system - 2:
            # player wins
            games.append(f"{score - 2}:0")
        elif point == "L" and score == -system + 2:
            # opponent wins
            games.append(f"0:{score + 2}")
        elif point == "W" and score == system - 1:
            # score is tied
            games.append(f"{score - 1}:{score - 1}")
        elif point == "L" and score == -system + 1:
            # score is tied
            games.append(f"0:{score + 1}")

        if point == "W":
            last_points_won = "W"
        else:
            last_points_won = "L"

    if last_points_won == "W":
        current_game = "".join(current_game)
        games.append(f"{current_game}")
    else:
        current_game = "".join(current_game)
        games.append(f"{current_game}")

    return games
def test_calculate_score():
    # Test case 1: A single game in both systems, with a clear winner.
    points = "WWWWWWWWWWL"
    expected_11 = ["10:1"]
    expected_21 = ["10:1"]
    assert calculate_score(11, points) == expected_11, "Test case 1 (11-point) failed"
    assert calculate_score(21, points) == expected_21, "Test case 1 (21-point) failed"

    # Test case 2: Multiple games, some completed and one in progress.
    points = "WWLWWLWWLWWLWE"
    expected_11 = ["9:4"]
    expected_21 = ["9:4"]
    assert calculate_score(11, points) == expected_11, "Test case 2 (11-point) failed"
    assert calculate_score(21, points) == expected_21, "Test case 2 (21-point) failed"

    # Test case 3: A longer sequence with many games and a final unfinished game.
    points = "WWLWLWLWLWLLWLWLWLWLWWLWWLWWLWLE"
    expected_11 = ['12:10', '5:4']
    expected_21 = ['17:14']
    assert calculate_score(11, points) == expected_11, "Test case 3 (11-point) failed"
    assert calculate_score(21, points) == expected_21, "Test case 3 (21-point) failed"

    print("All test cases passed!")

# Run the test function
test_calculate_score()