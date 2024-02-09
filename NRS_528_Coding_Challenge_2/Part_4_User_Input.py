# Coding Challenge 2: Part 4

# Ask the user for an input of their current age
# Tell them how many years until they reach retirement (65 years old).
# Here's a hint:
# age = input("What is your age?")
# print("Your age is" + str(age))

age = int(input("What is your age?"))
retirement_age = 65
years_until_retirement = (retirement_age - age)
print("Congrats! We get to plan your retirement party in " + str(years_until_retirement) + " years!")

#######

# I'm guessing putting 'int' in front of an input function
# tells the computer to expect an integer.
