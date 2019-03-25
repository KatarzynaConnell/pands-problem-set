# Kasia Connell, 2019
# Solution to question 6
# The program will take user's input string and output every second word

# References: 
# Ian's video tutorials: https://web.microsoftstream.com/video/909896e3-9d9d-45fe-aba0-a1930fe08a7f
# Programiz: https://www.programiz.com/python-programming/methods/string/join
# Stackoverflow: https://stackoverflow.com/a/54857192
# Python Documentation: https://docs.python.org/3/library/string.html
# 
# # enter the command in Cmder 'python solution-6.py'

# User is asked to enter a string of text
string = (input("Enter a string of text:"))
p = string.split()[::2]             # using string split function to separate string into words and get every second word by using [::2]
separator = ' '                     # split function results in words with commas so separator 
print(separator.join(p))