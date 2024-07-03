#!/usr/bin/python3
name = input("What is your name? ")

name = name .strip()
# this removes leading and trailing spaces

name = name .capitalize()
# this capitalizes ONLY the very first letter of the string
# so if we don't remove the leading spaces first, it won't capitalize the first letter

name = name.title()
# this capitalizes the first letter of each word just like a title!
# therefore, spaces don't matter here

name = name.strip().capitalize()
# we can do this in one line but it's done in order so we have to use .strip() first

# we can also put all of these string manipulating methods in the line of the input
# like this: name = input("What is your name? ").strip().capitalize()
print("Hello, " + name + "!")
#here we have to put a space after Hello because + only concatenates
#Both the string and the name are considered one argument
print("Hello,", name + "!")
#here we don't have to put a space because , adds a space and separates the arguments
print ("Hello, {}!".format(name))
print (f"Hello, {name}!")
# all of these do the same thing
# _______________________________________________________________________________________________________

name = input("What is your name? ")

first, last = name.split(" ")
# split() separates the string using the space as the delimiter
# the first split string is the first name, the second split string is the last name
# here the assignment goes from left to right
# if you give it two words separated by many spaces, it'll throw an error
# that there's supposed to be only two substrings
print(f"Hello, {first}!")
# we can use each one of them separately

"""
Notes:
    - Parameters: are what the function CAN TAKE
    - Arguments: are what you'll actually PASS to a function
    - There are two types of parameters: Positional parameters and keyword (named) parameters

        - Positional parameters: are the parameters that are in the order they are written
          ya3ny masalan awel string hndyh le print hytb3 el awel, b3den el tany wel talet,..etc.

        - Keyword (named) parameters: are the parameters that are written with a name like sep=' ' and end='\n'

    Print(*objects, sep = ' ', end = '\n', file = None, flush = False)
        *objects: any number of objects
        sep: separator between the objects
        end: the string to be printed after the last object
    docs.python.org: is where you can find the documentation
"""
