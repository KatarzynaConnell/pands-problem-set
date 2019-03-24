# Kasia Connell, 2019
# Solution to question 6
# The program will take user's input string and output every second word

# References: 
# Ian's video tutorials: https://web.microsoftstream.com/video/909896e3-9d9d-45fe-aba0-a1930fe08a7f
# Stackoverflow:https://stackoverflow.com/a/54857192 
# Python Documentation: https://docs.python.org/3/library/string.html
# 
# # enter the command in Cmder 'python solution-6.py'

# User is asked to enter a string of text
s = str(input("Enter a string of text:"))
t = s.split(' ')[::2]           # split function to split string into words and next get every second word using []::2]
print(t)                        # print the output