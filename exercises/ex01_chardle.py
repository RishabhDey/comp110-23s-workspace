"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730558424"

x = input("Enter a 5-character word: ")
if (len(x) != 5):
    print("Error: Word must contain 5 characters")
    quit()
sx = input("Enter a single character: ")
if (len(sx) != 1):
    print("Error: Character must be a single character.")
    quit() 
print("Searching for " + sx + " in " + x)


total = 0
if (x[0] == sx):
    total += 1
    print(sx + " found at index 0")
if (x[1] == sx):
    total += 1
    print(sx + " found at index 1")
if (x[2] == sx):
    total += 1
    print(sx + " found at index 2")
if (x[3] == sx):
    total += 1
    print(sx + " found at index 3")
if (x[4] == sx):
    total += 1
    print(sx + " found at index 4")


if (total == 1):
    print("1 instance of " + sx + " found in " + x)
elif (total == 0):
    print("No instances of " + sx + " found in " + x)
else:
    print(str(total) + " instances of " + sx + " found in " + x)
