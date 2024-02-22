# Coding Challenge 3: Part 2

# Construct a rudimentary Python script that takes a series of inputs from a bat file,
#   and does something to them.
# The rules:
#   1. Minimum of three arguments to be used.
#   2. You must do something simple in 15 lines or fewer within the Python file.
#   3. Print or file generated output should be produced.

import sys

Letter_Values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
                 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
                 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
                 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
                 'y': 4, 'z': 10}


def calculate_scrabble_score(word_combo):
    points = 0
    for letter in word_combo:
        for key in Letter_Values:
            if letter in key:
                points += Letter_Values[key]
                break
    return points


word = sys.argv[1].lower()
points = calculate_scrabble_score(word)
print(f"The Scrabble score for '{str(word)}' is {int(points)}.")

word = sys.argv[2].lower()
points = calculate_scrabble_score(word)
print(f"The Scrabble score for '{str(word)}' is {int(points)}.")

word = sys.argv[3].lower()
points = calculate_scrabble_score(word)
print(f"The Scrabble score for '{str(word)}' is {int(points)}.")

# This code is from the 'ArcGIS Python - Revisiting sys.argv and the Windows bat File' Video.
# I used the dictionary from my own Coding Challenge 2 though.

# Today I learned - Pycharm wants function names to be in lowercase, apparently.
# def = define
# 'word_combo' is just a variable, so are 'key' and 'letter'.
# Also, today I learned: hover over orange text to find out what it does in the code.
# Argument = short for 'Command Line Argument'

# Each argument is separated by a space

# sys.argv listens for arguments in a .bat file and spits out a list,
#   which puts the arguments and the format given in the Python file together.

# The advantage of doing it this way is to avoid using the command prompt for everything.
#   Makes it way easier if you need to make changes or delete something on the fly.

# Each argument needs its own use of sys.argv and its own index number, in list formation

# Remember, 'return' lets the dog give you the stick they just fetched
#   Otherwise, you're not getting the result/stick you wanted from a 'for' loop

# If we're trying to call commands within a string, it looks like we use squiggly brackets,
#   because Python code will treat a square or round bracket as part of the string,
#   but I noticed that's not the case for squiggly brackets.
#   By the way, pretty sure this is called 'nesting'.

# The addition of '.lower' to a use of 'sys.argv' puts the string outputs in lowercase,
#   and this is particularly useful if case sensitivity could be an issue.
#   Conversely, '.upper' puts them all in uppercase, but why do that unless you're yelling?

# The plus-equals operator (+=):
#   provides a convenient way to add a value to an existing variable
#   and assign the new value back to the same variable (Codecademy)

#  Dang it, this turned out to be more than 15 lines. At least I get it now :)
