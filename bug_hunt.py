# BUG: Added the missing quotation mark.
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: Corrected the variable name using an f-string.
print(f"Nice to meet you, {name}")

age = input("How old are you? ")

# BUG: Converted age to integer before adding 1.
print("Next year you will be " + str(int(age) + 1))