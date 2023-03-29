"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730558424"

pre = "python"
bools = True
i = 0
final = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess = input(f"What is your {len(pre)}-letter guess? ")
while bools: 
    if (len(guess) == len(pre)):
        bools = False
    else:
        guess = input(f"That was not {len(pre)} letters! Try again: ")


while i < len(pre):
    if (pre[i] != guess[i]):
        i2 = 0
        cond = False
        while i2 < len(pre):
            if (guess[i] == pre[i2]):
                final += f"{YELLOW_BOX}"
                cond = True
                break
            else:
                i2 += 1
        if (cond is False):
            final += f"{WHITE_BOX}"

    else:
        final += f"{GREEN_BOX}"
    i += 1
print(final)

if (pre == guess):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
