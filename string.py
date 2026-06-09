#string is a data type in python which is used to store text data. 
# It is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Strings are immutable, meaning that once a string is created, it cannot be modified.

#1. creation of string
# string1 = "Hello, World!"
# print(string1)

# #2. accessing characters in a string
# print(string1[0])  # Output: H
# print(string1[7])  # Output: W

# #3. updating a string
# # Since strings are immutable, you cannot update or modify their characters directly.
str1 = "Python-Programming"
print(str1)
# However, you can create a new string by concatenating existing strings or by using string methods.
# Example of concatenating strings  
str2 = " is fun!"
new_str = str1 + str2
print(new_str)  # Output: Python-Programming is fun!