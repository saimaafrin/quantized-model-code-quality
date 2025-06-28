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

    def increment_points(point_type):
        """Increment the player's score if point type is 'W', else increment opponent's score"""
        nonlocal player_score
        nonlocal opponent_score
        if point_type == "W":
            player_score += 1
        else:
            opponent_score += 1

    def finish_game(player_score, opponent_score):
        """Return a tuple of the player's score and the opponent's score if the game is finished"""
        nonlocal system
        if (
            (player_score - opponent_score >= 2)
            and (player_score >= system)
            and (opponent_score >= system)
        ):
            return f"{player_score}:{opponent_score}"
        else:
            return None

    player_score = 0
    opponent_score = 0
    game_scores = []

    # check if the game is finished (by looking at the last point in the sequence)
    if points[-1] == "W":
        player_score += 1
    else:
        opponent_score += 1

    if finish_game(player_score, opponent_score) is not None:
        return [finish_game(player_score, opponent_score)]

    # loop through the sequence of points and add each point to the respective score
    for point in points:
        increment_points(point)
        if finish_game(player_score, opponent_score) is not None:
            game_scores.append(finish_game(player_score, opponent_score))
            player_score = 0
            opponent_score = 0

    # if the game is still not finished, add the current score to the list of game scores
    if finish_game(player_score, opponent_score) is None:
        game_scores.append(f"{player_score}:{opponent_score}")

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