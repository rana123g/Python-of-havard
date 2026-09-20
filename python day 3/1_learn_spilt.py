# Ask user for their name
name = input("Enter your name: ")
# Split the user full name 
# If the user name is a bit long we can arrange it like that
#Here the 1 means that split at only the first space and leave the rest as it is:


first , last = name.split(" ", 1)
#print the user name
print(f"Hello, {last}")

