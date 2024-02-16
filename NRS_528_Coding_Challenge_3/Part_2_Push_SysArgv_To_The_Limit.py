# Coding Challenge 3: Part 2

# Construct a rudimentary Python script that takes a series of inputs from a bat file,
#   and does something to them.
# The rules:
#   1. Minimum of three arguments to be used.
#   2. You must do something simple in 15 lines or less within the Python file.
#   3. Print or file generated output should be produced.

# When creating a batch file, start out with the python interpreter filepath.
# Then afterwards, add the Python file you want the batch file to interface with (?)
# Then list your arguments on one line (?)
# Do all three steps on one line. On the next line, type 'pause'
#   so it doesn't immediately close out.

#######

import sys

print("Pizza Topping 1 = " + str(sys.argv[1]))
print("Pizza Topping 2 = " + str(sys.argv[2]))
print("Pizza Topping 3 = " + str(sys.argv[3]))

