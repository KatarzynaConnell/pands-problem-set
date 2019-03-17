# Kasia Connell, 2019
# Solution to question 2
# The program will output whether or not today is a day that begins with the letter T.

# References: Ian's video tutorials: https://web.microsoftstream.com/video/cd3347c4-8296-4e8c-bb63-01ef5452de17
# Enter the command in Cmder 'python Solution-2.py'

# function to get the current date and time from the time zone database
import datetime

if datetime.datetime.today().weekday() == 1:    # if today is Tuesday
  print("Yay! Today begins with the letter T!")

if datetime.datetime.today().weekday() == 3:    # if today is Thursday
 print("Yay! Today begins with the letter T!")

else:                                           # if today is not Tuesday or Thursday   
  print("No, today does not start with T.")