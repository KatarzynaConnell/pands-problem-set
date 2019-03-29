# Kasia Connell, 2019
# Solution to Question 8
# The program will output today's date and time in the format "Monday, January 10th 2019 at 1.15pm"
# Refernces: 
# Ian's video tutorial https://web.microsoftstream.com/video/b8925ffa-0cf5-4fff-bfb0-b4664f704879
# Ian's video tutorial https://web.microsoftstream.com/video/521b97db-d935-4351-a748-77f044770f24
# https://docs.python.org/3/library/datetime.html

# enter the command in Cmder 'python solution-8.py'
import datetime as dt   # import datetime module to be able to use all the functionality in the module and call it dt 

# the function datetime.now is entered to source the current time and date strftime allows to set conditions day number format 
day = (dt.datetime.now().strftime(" %d"))
if day == (1, 21, 31): # if day is equal to 1, 21 or 21 the output will show "st"

    Ord = "st"

if day == (2, 22):      # if day is equal to 2, 22 the output will show "nd"

    Ord = "nd"

if day == (3, 23):      # if day is equal to 3, 23 the output will show "rd"

   Ord = "rd"

else:

    Ord = "th"          # for any other day the output will show "th"
# format date into string using date format specifier and formatted string (date format specifier to format day to ordinal number)
# Adapted from https://docs.python.org/3/library/datetime.html and Ian's video about fstrings
today = dt.datetime.strftime(dt.datetime.now(), f"%A, %B %d{Ord} %Y at %I.%M%p") # function that allows formatting the date and time in a specific way, 

print(today)        # print the result