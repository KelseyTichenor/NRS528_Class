# Coding Challenge 2: Part 1

# We'll use this list for the very first Python file ever:
# [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]

#######

# Part 1:
# Make a new list that has all the elements less than 5 from the above list in it
# Print out this new list

Item_1_List = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]


def numbers_less_than_5(variable):
    return variable < 5


filtered_numbers = filter(numbers_less_than_5, Item_1_List)

print("First filtered list: " + str(list(filtered_numbers)))

#######

# What did I learn here?
# (Sorry if this is tedious - writing/typing helps me digest and retain information.)
# Feel free to skip to Part 2 if you just want the good stuff :D

# Step 1: What is 'def'?
#   def = short for 'define', pertains to variables / functions
#         should be the first step, so the computer has a reference to work with.
# Step 2: Name the function and the variable (something that isn't 'i', preferably)
# Step 3: What is 'return'?
#   return = asks for a function's output,
#            then defines what the output should be,
#            then attaches the desired output to the function that was just defined
# Step 4: What is 'filter'?
#   filter = applying the parameters of a previously defined list to a larger list,
#            and expecting a new list of filtered results to pop out
#            The filtered list is also given a name.
# Step 5: List (as a command) = create a list based off the name of the filter (I think?)
#         Print = make the computer spit out a visual output of the code you just coded

#######

# Part 2:
# Do the same thing as Part 1, but do it all in one line of code. O_O

filtered_numbers = filter(lambda variable: variable < 5, Item_1_List)
print("Same result, but with one line of code: " + str(list(filtered_numbers)))

#######

# Note: I guess 'lambda' is called the 'anonymous function' (according to Google)
#       It can apparently be used in many contexts, but I'm not too sure what they all are.
#       Not yet, anyway.
