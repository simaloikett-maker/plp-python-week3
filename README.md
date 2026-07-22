# Assignment: Name Splitter, Bug Hunt & First Decisions

## Files

### name_greeter.py
Uses `.split()` to separate a user's full name and greets them by their first name if they enter two or more names.
If only one name is entered, it asks for their full name.

### bug_hunt.py
Fixes the three bugs in the provided program and includes `# BUG:` comments explaining each correction.

### ticket_checker.py
Checks whether the user is an adult using a Boolean expression and displays the appropriate ticket price.

## Reflection

The bug that took the longest to find was the age calculation because Python could not add a string and an integer together. 
The error message clearly showed that the values had different data types, helping me realize I needed to convert the age to an integer before adding
1. Fixing one error at a time made the debugging process much easier.
