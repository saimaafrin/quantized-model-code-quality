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
    # Split the string of points into a list
    points = list(points)
    # Initialize an empty list to hold game scores
    game_scores = []
    # Initialize a variable to hold the player's current score
    player_score = 0
    # Initialize a variable to hold the opponent's current score
    opponent_score = 0
    # Iterate over each point in the sequence
    for point in points:
        # If the point is a player win (W), add 1 to the player's current score
        if point == 'W':
            player_score += 1
        # If the point is an opponent win (L), add 1 to the opponent's current score
        else:
            opponent_score += 1
        # If the player has a 2-point lead and has reached the system's required number of points,
        # add the player's score to the list of game scores and reset both player and opponent scores
        if player_score - opponent_score >= 2 and player_score >= system:
            game_scores.append(f"{player_score}:{opponent_score}")
            player_score = 0
            opponent_score = 0
        # If the opponent has a 2-point lead and has reached the system's required number of points,
        # add the opponent's score to the list of game scores and reset both player and opponent scores
        elif opponent_score - player_score >= 2 and opponent_score >= system:
            game_scores.append(f"{player_score}:{opponent_score}")
            player_score = 0
            opponent_score = 0
    # If the sequence ends in the middle of a game, add the current score to the list of game scores
    if player_score != 0 and opponent_score != 0:
        game_scores.append(f"{player_score}:{opponent_score}")
    # Return the list of game scores
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