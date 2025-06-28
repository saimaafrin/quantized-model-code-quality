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
    player_score = 0
    opponent_score = 0
    player_lead = 0
    opponent_lead = 0
    game_scores = []
    game_points = 0

    for i, point in enumerate(points):
        if point == "W":
            player_score += 1
        elif point == "L":
            opponent_score += 1

        game_points += 1

        if system == 11:
            if player_score == 10:
                if opponent_score < 4:
                    game_scores.append(f"{player_score}:{opponent_score}")
                elif opponent_score < 6:
                    player_lead += 1
                elif opponent_score < 10:
                    opponent_lead += 1
                if player_lead > 1 and opponent_lead > 1:
                    break

            elif opponent_score == 10:
                if player_score < 4:
                    game_scores.append(f"{player_score}:{opponent_score}")
                elif player_score < 6:
                    opponent_lead += 1
                elif player_score < 10:
                    player_lead += 1
                if player_lead > 1 and opponent_lead > 1:
                    break

        elif system == 21:
            if player_score == 20:
                game_scores.append(f"{player_score}:{opponent_score}")
                break
            elif opponent_score == 20:
                game_scores.append(f"{player_score}:{opponent_score}")
                break

        if game_points == system:
            game_points = 0
            player_score = 0
            opponent_score = 0
            player_lead = 0
            opponent_lead = 0

    return game_scores
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