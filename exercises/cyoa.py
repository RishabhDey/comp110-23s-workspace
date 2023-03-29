"""I am uncreative - EX06."""
import random
points: int
player: str
emoji = "'\U0001F603"


def main():
    """Main procedure."""
    global points
    global player
    global emoji 
    greet()
    while True:
        x = input(f"Would you like a procedure or function or to quit{emoji}?")
        if (x == "procedure"):
            custom_procedure()
        elif (x == "function"):
            points += custom_function()
        elif (x == "quit"):
            break
        print(f"Hi {player}, you now have {points} points.")


def greet() -> None:
    """Greeting."""
    global player 
    player = input("This is your adventure. What is your name?")
    print(f"Hi {player}, welcome to this game!")
    

def custom_procedure() -> None:
    """Procedure."""
    global player
    global points
    
    x = input(f"Do you want points right now {player}?")
    
    if (x == "yes"):
        points += random.randrange(1, 10)
    else:
        points -= random.randrange(1, 10)
    return None
    

def custom_function() -> int:
    """Function."""
    global player
    x = input(f"Do you want points right now {player}?")
    if (x == "yes"):
        return random.randrange(1, 10)
    else:
        return -(random.randrange(1, 10))


if __name__ == "__main__":
    """Public function."""
    main()
