# Ask user for their name
name = input("What is your name: ")
#If I want that any space written accidently get's removed and there would be only one space
name = name.strip()
#If I want that it always capitalize the first leetter of anything written in the variable name and stored in it
name = name.capitalize()
#If I want to make that every letter after a space would be capatialze I can use this function
name = name.title()
# User an f-string to print the greeting
print(f"Hello, {name}")

#name.strip() For removing any unwanted spaces from the beginning and end of the string.
#name.capitalize() For capitalizing the first letter of the string.
#name.title() For capitalizing the first letter of each word in the string.
