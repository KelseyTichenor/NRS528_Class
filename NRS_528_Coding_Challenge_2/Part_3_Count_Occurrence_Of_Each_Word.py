# Coding Challenge 2: Part 3

# Given a single phrase, count the occurrence of each word:
# We'll be using the following string:
#   string = 'hi dee hi how are you mr dee'
# Count the occurrence of each word, and print the word plus the count.
# Here's a hint: you might want to "split" this into a list by a white space: " ".

Word_String = 'hi dee hi how are you mr dee'
Word_Occurrences_List = Word_String.split()
# print(Word_Occurrences_List)
from collections import Counter

Counter(Word_Occurrences_List)
print(Counter(Word_Occurrences_List))

#######

# First off: HOLY CRAP THAT WORKED!?
# We can turn a string into a list by adding '.split()' at the end of the string title.
# Note to self: find out what's in the 'collections' list
# Counter is used to count the occurrences in a list.
# Also: Line 12 - does 'from' really need to be at the top of the file?
