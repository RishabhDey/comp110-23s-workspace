"""Hi."""
def invert(x: dict[str, str]) -> dict[str, str]:
    """Invert."""
    keycheck = list(x.values())
    
    if(max(keycheck, key = keycheck.count) ==1):
        final = {x[key]: key for key in x}
        return final
    else:
        raise KeyError()


def favorite_color(x: dict[str, str]) -> str:
    """Fav."""
    return max(x.values(), key = list(x.values()).count)


def count(x: list[str]) -> dict[str, int]:
    """count."""
    final = {}
    
    for x1 in x:
        if(x1 in final):
            final[x1] +=1
        else:
            final[x1] = 1
            
    return final
