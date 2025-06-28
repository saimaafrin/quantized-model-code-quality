from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str, ...]:
    """
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    >>> bf('Jupiter', 'Neptune')
    ('Saturn', 'Uranus')
    >>> bf('Earth', 'Mercury')
    'Venus'
    >>> bf('Mercury', 'Uranus')
    ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
    """

    # use a set to check for correct planet names
    correct_planets = {'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'}

    # if either planet is not a correct planet name, return an empty tuple
    if planet1 not in correct_planets or planet2 not in correct_planets:
        return ()

    # order the planets in the solar system
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    # calculate the indexes of the planets in the order
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)

    # check for the case where planet1 or planet2 is closer to the sun than the other
    if planet1_index > planet2_index:
        planet1_index, planet2_index = planet2_index, planet1_index

    # return all planets between planet1_index and planet2_index, sorted by proximity to the sun
    return tuple(sorted(planets[planet1_index + 1: planet2_index + 1], key=planets.index))
