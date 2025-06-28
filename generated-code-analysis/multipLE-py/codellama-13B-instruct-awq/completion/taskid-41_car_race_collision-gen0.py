def car_race_collision(n: int) -> int:
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """

    if n <= 0:
        raise ValueError('Input must be a positive integer.')

    # Base cases:
    # When n = 1, there is no collision
    # When n = 2, there is one collision
    if n == 1 or n == 2:
        return n - 1

    # Recursive case:
    # Every time two cars collide, there is a new car that comes from the
    # opposite direction and starts at the same position as the car that
    # collided.  The number of collisions is the number of cars that
    # are in the same position plus the number of collisions in the
    # previous position.
    return car_race_collision(n - 1) + car_race_collision(n - 2)
