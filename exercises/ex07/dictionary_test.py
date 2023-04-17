"""Hi."""

import dictionary


def test_invert1():
    """Hi."""
    dictionary.invert({'a': 'hi', 'b': 'y', 'c': 'x'})


def test_invert2():
    """Hi."""
    dictionary.invert({'hi': 'cat'})


def test_invert3():
    """Hi."""
    dictionary.invert({'kris': 'hi', 'michael': 'jordan'})


def test_favorite_color1():
    """Hi."""
    dictionary.favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})


def test_favorite_color2():
    """Hi."""
    dictionary.favorite_color({"Marc": "yellow", "Ezri": "yellow", "Kris": "yellow"})


def test_favorite_color3():
    """Hi."""
    dictionary.favorite_color({"Marc": "green", "Ezri": "green", "Kris": "blue"})   


def test_count1():
    """Hi."""
    dictionary.count([1, 4, 3, 2, 1])


def test_count2():
    """Hi."""
    dictionary.count([1, 4, 3, 2, 3])


def test_count3():
    """Hi."""
    dictionary.count([4, 4, 3, 4, 1])
