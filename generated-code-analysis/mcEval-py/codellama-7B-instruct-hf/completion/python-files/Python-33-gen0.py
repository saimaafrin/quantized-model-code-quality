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

    # Initialize empty lists to store scores and game lengths
    scores = []
    lengths = []

    # Store the length of the string
    string_length = len(points)

    # Initialize counters for the player's score and the opponent's score
    player_score = opponent_score = 0

    # Initialize a counter to keep track of the current game's length
    game_length = 0

    # Iterate through the string
    for i in range(string_length):

        # Check if the current character is a 'W'
        if points[i] == "W":

            # If the current character is a 'W', increment the player's score
            player_score += 1

            # Increment the current game's length
            game_length += 1

        # Check if the current character is an 'L'
        elif points[i] == "L":

            # If the current character is an 'L', increment the opponent's score
            opponent_score += 1

            # Increment the current game's length
            game_length += 1

        # Check if the current character is a '.'
        elif points[i] == ".":

            # If the current character is a '.', append the current game's length to the game lengths list
            lengths.append(game_length)

            # Reset the current game's length to 0
            game_length = 0

            # Append the player's score and the opponent's score to the scores list, formatted as "player_score:opponent_score"
            scores.append(f"{player_score}:{opponent_score}")

            # Reset the player's score to 0
            player_score = 0

            # Reset the opponent's score to 0
            opponent_score = 0

    # Append the player's score and the opponent's score to the scores list, formatted as "player_score:opponent_score"
    scores.append(f"{player_score}:{opponent_score}")

    # Append the current game's length to the game lengths list
    lengths.append(game_length)

    # Calculate the total number of games played
    total_games = sum(lengths)

    # Calculate the number of games the player won
    player_games = sum(score.count("W") for score in scores)

    # Calculate the number of games the opponent won
    opponent_games = sum(score.count("L") for score in scores)

    # Calculate the difference between the number of games won by the player and the number of games won by the opponent
    game_diff = player_games - opponent_games

    # Check if the difference between the number of games won by the player and the number of games won by the opponent is less than or equal to 2
    if game_diff <= 2:

        #
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