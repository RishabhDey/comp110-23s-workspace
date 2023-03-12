"""EX04."""

__author__ = 730558424


def all(x: list[int], y: int) -> bool:
    """All."""
    if len(x) == 0:
        return False
        
    index = 0
    while (index < len(x) - 1):
        if (x[index] != y):
            return False
        index += 1
    return True


def max(x: list[int]) -> int:
    """Max."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
        
    index = 0
    max = x[0]
    
    while (index < len(x)):
        if (x[index] > max):
            max = x[index]
        index += 1    
    return max


def is_equal(x: list[int], y: list[int]) -> bool:
    """Is equal."""
    if (len(x) != len(y)):
        return False
    index = 0
    while (index < len(x) - 1):
        if (x[index] != y[index]):
            return False
        index += 1
        
    return True
