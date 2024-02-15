
#####
# Step 4 - Iteration
#####

# For Loops

# # For loop on string
# my_string = 'abcde'
# for i in my_string:
#     print(i)
# # Any code listed after the print function will be executed after the 'for' loop, AKA outside the loop
#
# For loop on list
# my_list = ['ab', 'b', 'c', 'd', 'e']
# for i in my_list:
#     print(i)
#
# # For loop on tuple
# my_tuple = ('a', 'b', 'c', 'd', 'e')
# for i in my_tuple:
#     print(i)
#
# # For loop on dictionary
# my_dictionary = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# for i, j in my_dictionary.items():
#     print(i, j)
# In this list, 1 is the key, a is the value
# We use the .items(): to let it know it needs to pull items from the dictionary
#
# If/else/elif

# You can use if/else/elif to make decisions based on your data:
# ALWAYS start with 'if'
# 'elif' is a secondary 'if', if you will
# else = catchall condition
# you don't always need 'elif', you always need an 'if'
# you can have as many elifs as you want.
# my_var = 11
# if my_var > 10:
#     print('Greater than 10')
# elif my_var == 5:
#     print('Equal to 5')
# else:
#     print('Less than 5')

# Using if to catch cases as we loop:
# my_if_list = [1, 2, 3, 4, 5, 6]
# for number in my_if_list:
#     if number % 2 == 0:
#         print(str(number) + ' is even because we can divide it by two')
#     else:
#         print(str(number) + ' is odd because it will not divide by two')

# Make sure you're printing everything, especially if you don't know what it does and want to find out
# Python Cheatsheet: really good Python resource
#
# While

# We can use while to perform some task
# i = 0
# while i < 10:
#     i = i+1
#     print(i)
#
# # Be careful though not to enter an infinite loop as you forgot your increment
# i = 0
# while i < 10:
#     print(i)
# This is why we NEED print statements though, because if you don't, it's gonna show no data
# while your computer keeps using ram and GPU resources and stuff


