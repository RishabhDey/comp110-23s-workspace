import dictionary

def test_invert1():
    invert({'a': 'z', 'b' : 'y', 'c': 'x'})

def test_invert2():
    invert({'apple': 'cat'})

def test_invert3():
    invert({'kris': 'jordan', 'michael': 'jordan'})

def test_favorite_color1():
    favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"})

def test_favorite_color2():
    favorite_color({"Marc": "yellow", "Ezri": "yellow", "Kris": "yellow"})

def test_favorite_color3():
    favorite_color({"Marc": "green", "Ezri": "green", "Kris": "blue"})   

def test_count1():
    count([1, 4, 3, 2, 1])

def test_count2():
    count([1, 4, 3, 2, 3])

def test_count3():
    count([4, 4, 3, 4, 1])
