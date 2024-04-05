
#####
# Step 1 - Basic Functions
#####

# Functions are a fundamental coding tool in Python, they enable you to create blocks of
# code that can be repeatably used. Once written you can talk to the function multiple times
# with different inputs.

# Functions are defined using "def", followed by the function name and arguments in parentheses.
# the first line can be an optional statement that contains documentation about the function,
# aka docstring. Functions may have a "return" argument, which may return an output of the
# function but this is not essential. To call a function you would call the name of the function
# and provide the arguments, see the example below.


# def do_math(x,y):
#     """This is docstring, it can be used to explain what the function does."""
#     value = x + y
#     return value
# # indented things all belong to the do_math function
# def = defines the function as a function
# do_math = name of the function
# x and y are the arguments
# function ends with a return argument - not necessarily needed, but useful


# print(do_math(1, 2))
# print(do_math(10, 10))
# print(do_math(20, 50))

# Task 1 - Comment out the above code, and then uncomment and execute the below code, analyze the error,
# why did the code below not work?
# It didn't work because it's expecting an argument when we define the function, but we didn't give it an argument
#   in the print_me() parentheses

# def print_me(str):
#     """This prints a passed string into this function"""
#     print(str)
#     return
#
# print_me()

# Task 2 - Repair the code in the area below (Hint: do you need to edit the function or not?):
# giving it one argument fixes the code, giving it multiple arguments breaks the code in a different way

# Task 3 - Turn the code below into a function, and then run the code using the inputs: a and b (shown), and
# # i = s and j = e
#
# i = "a"
# j = "b"
#
# output = i + j + j + i
# print(output)

def word_maker(i,j):
    value = i +j + j + i
    i = 'a'
    j = 'b'
    return value

# does the function name actually mean anything? I think not - it's just a name

print(word_maker(a, b))
print(word_maker(s, e))