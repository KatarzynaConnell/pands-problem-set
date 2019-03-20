# Kasia Connell, 2019
# Solution to Question 5
# The program will ask use to enter positive integer and it will tell if the number is a prime number

# enter the command in Cmder 'python solution-5.py'

# Ask the user for positive integer
i = int(input("Enter a positive integer: "))   # The value of i is set to any positive integer

# References: Ian's video tutorial: https://web.microsoftstream.com/video/3ef695e3-9155-4487-b48e-0867834c76ad

# Use for loop to set the range of numbers to be checked in the if condition
for x in range(2, i):                   # range starts from 2 as it is the first prime number
    if i % x == 0:                      # if statement checks if there i a remainder 
        print(i, 'is not a prime number') # print the answer
        break                           # break is to stop further checks in the loop once one number is found (other than 1 or i) that i can be divided by with a remainder = 0 
else:                                   # connected to for loop - if for loop brought no result
    print(i, 'is a prime number')       # print the answer