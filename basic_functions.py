"""
Purpose: Illustrate basic functions in Python.

Author: Denise Case

This file name is:   basic_functions.py
This module name is: basic_functions

Functions

Functions are reusable bits of code.
Functions are defined using the def keyword.
Functions are called using the function name and parentheses.
Functions can accept parameters (arguments).
Functions can return values.

Built-in Functions

Python has many helpful built-in functions.

len() is a built-in function that returns the length of an object.
min() is a built-in function that returns the smallest item in an iterable.
max() is a built-in function that returns the largest item in an iterable.  

print() is a built-in function that prints to the screen.
input() is a built-in function that gets input from the user.

str() is a built-in function that converts a value to a string.
int() is a built-in function that converts a value to an integer.

@ uses webbrowser module to open a web browser to a url
"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger
from datetime import date

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library

import webbrowser


# Declare Variables
url = "https://docs.python.org/3/library/functions.html"
number_list = [1, 2, 3, 4, 5]

# Use built-in functions like len(), min(), max()
length = len(number_list)
smallest = min(number_list)
largest = max(number_list)
hint = "HINT: In the terminal, hit up arrow to rerun a command and try again.\n"

# Log Information
logger.info(f"Functions url = {url}")
logger.info(f"number_list = {number_list}")
logger.info(f"len(number_list) = {length}")
logger.info(f"min(number_list) = {smallest}")
logger.info(f"max(number_list) = {largest}")

# Print an empty line to the terminal
print()

# Greet the user
print("Greetings!")

# Get the user's name and greet them
name = input("What's your name? (type your name and hit enter): ")
message = f"Hello {name.capitalize()}!"
print(message)
print()
logger.info(f"message = {message}")

# Ask the user if they want to see built-in functions
response = input("Would you like to see all the built-in functions? (y/n) ").lower()
logger.info(f"response = {response}")
print(f"You said {response}!")
print(f"{hint}")

if response == "y":
    print()
    print("Let's open a web page. Python makes it easy!")
    webbrowser.open_new(url)
    print()
    print("There's a lot of built-in functions ready to use!")
    print("We'll learn more about them later.")
    print()

response2 = input ("Would you like to know today's date?(y/n)"). lower()
logger.info(f"response2 = {response2}")
print(f"You said {response2}!/")
print(f"{hint}")

if response2 == "y":
    print()
    print(f"Today's date is {date.today()}")
    print()
else:
    print()
    print(f"Thank you {name}")
# TODO: Run with different responses n, y, other...
