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
    # Initialize variables
    current_game_score = [0, 0]
    game_scores = []
    player_won = False

    # Go through the points
    for point in points:
        # If the game is still ongoing
        if current_game_score[0] + current_game_score[1] < system:
            if point == "W":
                current_game_score[0] += 1
            else:
                current_game_score[1] += 1

            # Check if one player has reached the required number of points
            if current_game_score[0] == system - 1 or current_game_score[1] == system - 1:
                # Check if there is a 2-point lead
                if abs(current_game_score[0] - current_game_score[1]) >= 2:
                    player_won = True

        # Game has ended
        else:
            # Check if the player has won
            if current_game_score[0] == system and current_game_score[1] == system - 1:
                player_won = True

            # Add the score to the list
            game_scores.append(f"{current_game_score[0]}:{current_game_score[1]}")

            # Initialize a new game
            current_game_score = [0, 0]

            # Check if the next point is a win
            if point == "W":
                current_game_score[0] += 1
            else:
                current_game_score[1] += 1

    # Check if the last game has ended
    if current_game_score[0] + current_game_score[1] == system:
        # Check if the player has won
        if current_game_score[0] == system and current_game_score[1] == system - 1:
            player_won = True

        # Add the score to the list
        game_scores.append(f"{current_game_score[0]}:{current_game_score[1]}")
    # If the game is still ongoing
    else:
        # Add the score to the list
        game_scores.append(f"{current_game_score[0]}:{current_game_score[1]}")

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