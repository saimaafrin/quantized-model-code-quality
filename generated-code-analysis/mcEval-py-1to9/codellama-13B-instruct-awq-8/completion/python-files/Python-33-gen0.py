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

    # set the default score to 0
    player_score = 0
    opponent_score = 0

    # set a variable to keep track of the current game state
    game_state = 0

    # set the default score limit to 11
    score_limit = 11

    # if the system is 21, set the score limit to 21
    if system == 21:
        score_limit = 21

    # create an empty list to store the game scores
    game_scores = []

    # iterate over the points string
    for point in points:

        # if the game is in progress, add a point to the current score
        if game_state == 1:

            # if the current score is 11, set the game state to 2 (meaning the game is in progress and the opponent has a 2-point lead)
            if player_score == score_limit - 1:
                game_state = 2

            # increment the current score
            player_score += 1

            # if the opponent has scored and the game state is 2, add a point to the opponent's score
            if point == "L" and game_state == 2:
                opponent_score += 1

        # if the current score is 11 or 21, add the score to the game scores and set the game state to 0 (meaning no game is in progress)
        if player_score == score_limit:
            game_scores.append(f"{player_score}:{opponent_score}")
            game_state = 0

        # if the current score is 0 and the game state is 2, add the score to the game scores and set the game state to 0 (meaning no game is in progress)
        elif player_score == 0 and game_state == 2:
            game_scores.append(f"{player_score}:{opponent_score}")
            game_state = 0

        # if the point is a 'W', add a point to the current score and set the game state to 1 (meaning the game is in progress and the player has a 2-point lead)
        elif point == "W":
            player_score += 1
            game_state = 1

    # return the list of game scores
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