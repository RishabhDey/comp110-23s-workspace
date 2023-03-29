"""Hi."""
__author__ = "730558424"
from exercises.ex05.utils import only_evens, sub, concat


def test_only_even1():
    """Hi."""
    return only_evens([1, 2, 3, 4])


def test_only_even2():
    """Hi."""
    return only_evens([4, 4, 3, 4])


def test_only_even3():
    """Hi."""
    return only_evens([4, 4, 4, 4])


def test_concat1():
    """Hi."""
    return concat([1, 2, 3, 4], [1, 3, 3, 4])


def test_concat2():
    """Hi."""
    return concat([4, 2, 5, 4], [1, 2, 3, 1])


def test_concat3():
    """Hi."""
    return concat([1, 2, 3, 4], [1, 3, 3, 6])


def test_sub1():
    """Hi."""
    return sub([4, 4, 4, 4], 1, 3)


def test_sub2():
    """Hi."""
    return sub([4, 4, 4, 4], 1, 4)


def test_sub3():
    """Hi."""
    return sub([4, 4, 4, 4], 0, 4)
