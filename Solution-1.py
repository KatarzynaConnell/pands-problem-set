# Kasia Connell, 2019
# Solution to question 1
# The program will ask user to enter any positive integer and it will output the sum of all the numbers between one and that number

# Ask the user for positive integer
i = int(input("Enter a positive integer: "))   # The value of i is set to any positive integer

# Create a new value of 'total' and set it to 0 
total = 0 

# References: https://web.microsoftstream.com/video/20963781-2aea-4302-ba73-5b8f327f4189

while i > 0 :   # i is positive integer larger than 0 - this is the checking statement
    total = total + i # take total on the right, add the current value of i to it, and override the new value of total on the left
    i = i - 1 # take 1 away from the value of i - I want next time to come back with the smaller value of i and get closer to the condition that i > 1 is false

print(total) # show the result on the screen