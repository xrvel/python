# Getting the user's name and age
name = input("What is your name? ")
age = int(input("How old are you, {}? ".format(name)))  # Convert the input string to an integer

# Checking the age and displaying a message
if age >= 18:
	print("Hello, {}! You are an adult.".format(name))
else:
	print("Hello, {}! You are not an adult.".format(name))