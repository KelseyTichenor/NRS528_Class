# Coding Challenge 2: Part 2

# For this file, we'll be using these lists:
# list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
# list_b = ['dog', 'hamster', 'snake']

#######

# Part 1:
# Determine which items are present in both lists.

list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
intersection = set(list_a) & set(list_b)
print("Overlapping Words: " + str(intersection))


#######

# Not going to lie, Pycharm definitely auto-completed this part for me
# Not complaining!
# Set = put all the items in a list under one big umbrella of a variable

#######

# Part 2:
# Determine which items do not overlap in the lists

def symmetric_difference(list_a, list_b):
    return list(set(list_a) - set(list_b)) and list(set(list_b) - set(list_a))


print("Non-Overlapping Words:" + str(((symmetric_difference(list_a, list_b)),
                                      (symmetric_difference(list_b, list_a)))))

#######

# symmetric_difference defines the parts of the lists that don't overlap
# return = ask for function output, then define what you're expecting
