# Kasia Connell, 2019
# Solution to question 1
# The program will ask user to enter any positive integer and it will output the sum of all the numbers between one and that number

# enter the command in Cmder 'python solution-1.py'

i = int(input("Enter a positive integer: ")) # i is any positive integer

total = 1 # running total while I am doing the calculation - set to 0 initially

while i > 1 :   # i is positive integer larger than 1
    total = total + i #take total on the right, add the current value of i to it, and override the new value of total on the left
    i = i - 1 # I want next time to come back with the smaller value of i

print(total)
