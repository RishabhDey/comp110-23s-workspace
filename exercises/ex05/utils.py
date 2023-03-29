"""Hi."""

__author__ = "730558424"


def only_evens(x: list[int]) -> list[int]:
    """Hi."""
    finalx = []
    for x1 in x: 
        if (x1 % 2 == 0):
            finalx.append(x1)
    return finalx     


def concat(x: list[int], y: list[int]) -> list[int]:
    """Hi."""
    final = []
    for x1 in x:
        final.append(x1)
    for y1 in y:
        final.append(y1)
    
    return final


def sub(x: list[int], xSI: int, xEI: int) -> list[int]:
    """Hi."""
    final = []
    if (xSI < 0):
        xSI = 0
    if (xEI > len(x)):
        xEI  = len(x)
    for ix in range(xSI, xEI):
        final.append(x[ix])
        
    return final
