# Kasia Connell, 2019
# Solution to Question 8
# The program will output today's date and time in the format "Monday, January 10th 2019 at 1.15pm"
# Refernces: 
# Ian's video tutorial https://web.microsoftstream.com/video/b8925ffa-0cf5-4fff-bfb0-b4664f704879
# https://docs.python.org/3/library/datetime.html

# enter the command in Cmder 'python solution-8.py'
import datetime as dt   # import datetime module to be able to use all the functionality in the module and call it dt 
dt.datetime.now()       # the function datetime.now is entered to source the current time and date

# format date into string using date format specifier
# Adapted from https://docs.python.org/3/library/datetime.html
today = dt.datetime.strftime(dt.datetime.now(), "%A, %B %d %Y at %H.%M%p") # function that allows formatting the date and time in a specific way, 

print(today)        # print the result