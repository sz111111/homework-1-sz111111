# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 06:46:59 2024

@author: ChelseySSS
"""

# PPHA 30537
# Spring 2024
# Homework 1

# SHIHAN ZHAO
# sz111111

# Due date: Sunday April 7th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

# Sample list of objects
sample_list = ['j', 'k', 'x', 'z']

# Loop through the list and print the required output
for index, obj in enumerate(sample_list):
    print(f"The value at position {index} is {obj}")


# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

# List of test strings
test_strings = ["radar", "A man, a plan, a canal, Panama!", "Microsoft", "This isn't a palindrome"]

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    clean_s = ''.join(char for char in s if char.isalnum()).lower()
    # Check if the cleaned string is equal to its reverse
    return clean_s == clean_s[::-1]

# Test the function with the provided strings
for test_str in test_strings:
    result = "is a palindrome" if is_palindrome(test_str) else "is not a palindrome"
    print(f"'{test_str}' {result}")



# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.

available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']

while True:
    choice = input('Please pick a vegetable I have available: ')
    if choice in available_vegetables:
        print(f'You can have the {choice}.')
        break
    else:
        print('Invalid choice, please pick a vegetable from the list.')


# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.

sample_strings = ['Apple', 'Banana', 'cranberry', 'pear', 'Grape', 'avocado', 'berry', 'Cherry']

modified_list = [s.lower() for s in sample_strings if not s.lower().startswith(('a', 'b'))]
print(modified_list)

# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}

short_names = ['IL', 'IN', 'MI', 'WI']
long_names = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']

state_dict = {short: long for short, long in zip(short_names, long_names)}
print(state_dict)

#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

def categorize_sum(num1, num2):
    total = num1 + num2
    if total > 10:
        return "big"
    elif total == 10:
        return "just right"
    else:
        return "small"

result_list = [categorize_sum(num1, num2) for num1, num2 in start_list]
print(result_list)


# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 40
    return a + b
x = my_func()


# Define the function with an argument and no global variable
def my_func(a, b=40):  
    return a + b

# Example usage
x = my_func(10)
print(x)


# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
#import random
#from numpy import random

import random

def generate_password(length, special_chars=True, include_numbers=True):
    # Define character sets
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    special_characters = '!@#$%^&*'
    
    # Combine character sets based on function arguments
    char_set = upper_case + lower_case
    if include_numbers:
        char_set += numbers
    if special_chars:
        char_set += special_characters
    
    # Check password length
    if 8 <= length <= 16:
        # Generate password
        password = ''.join(random.choice(char_set) for _ in range(length))
        return password
    else:
        # Print warning and exit
        return "Warning: Password length must be between 8 and 16."
    
# Example 
print(generate_password(12))
print(generate_password(7))  # This should print a warning
print(generate_password(12, special_chars=False))
print(generate_password(12, special_chars=False, include_numbers=False))
  

  
# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.

import random

# Define the MovieDatabase class
class MovieDatabase:
    def __init__(self, creator):
        self.creator = creator
        self.movies = []

    def add_movie(self, name, genre, rating):
        self.movies.append({'name': name, 'genre': genre, 'rating': rating})

    def what_to_watch(self):
        if not self.movies:
            print("No movies in the database yet!")
            return
        movie = random.choice(self.movies)
        print(f"Tonight, courtesy of {self.creator}, watch '{movie['name']}'! A {movie['genre']} rated {movie['rating']}/5.")

# Create an instance of MovieDatabase
my_database = MovieDatabase("SHIHAN ZHAO")

# Add four movies
my_database.add_movie("The Shawshank Redemption", "Drama", 5)
my_database.add_movie("The Godfather", "Crime", 5)
my_database.add_movie("Kung Fu Panda 4", "Animation", 3)
my_database.add_movie("Mad Max: Fury Road", "Action", 5)

# Call what_to_watch method
my_database.what_to_watch()




