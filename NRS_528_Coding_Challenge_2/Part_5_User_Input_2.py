# Coding Challenge 2: Part 5

# Using the following dictionary (or a similar one you found on the internet),
# ask the user for a word,
# and compute the Scrabble word score for that word
# steal this code from the internet, format it and make it work:
# letter_scores = {
#     "aeioulnrst": 1,
#     "dg": 2,
#     "bcmp": 3,
#     "fhvwy": 4,
#     "k": 5,
#     "jx": 8,
#     "qz": 10
# }

Scrabble_Word = str(input("What word would you like to play?"))
word_score = 0
Letter_Values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
                 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
                 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
                 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
                 'y': 4, 'z': 10}
for letter in Scrabble_Word:
    word_score += Letter_Values[letter]

print("This word is worth " + str(word_score) + " points.")

#######

# putting 'str' before an input function tells the computer to expect a string
# word score: need a base variable of 0 before we can think about adding letter values
# letter_values: can easily be put into a dictionary,
#                because each letter corresponds to its own value.
# += operator according to Google:
#       "provides a convenient way to add a value to an existing variable
#        and assign the new value back to the same variable"
