# Kasia Connell, 2019
# Solution to Question 4
# The program will ask user to enter positive integer and calculate the successive values as follows:
# check the current value - if even - divide it by 2, if odd - multiply it by 3 and add 1. 
# Keep the calculation ogoing. The program should end when the current value is 1. 

# References:
# Ian's video tutorials: https://web.microsoftstream.com/video/20963781-2aea-4302-ba73-5b8f327f4189
# Ian's video tutorials: https://web.microsoftstream.com/video/3ef695e3-9155-4487-b48e-0867834c76ad
# Ian's video tutorials: https://web.microsoftstream.com/video/82894055-5147-487d-ab35-6bf5c51cd889

# enter the command in Cmder 'python solution-5.py'

# Ask the user for positive integer
i = int(input("Enter a positive integer: "))   # The value of i is set to any positive integer

# used while loop to repeat the execution of the code as long as the condition is true
while i > 1:            # i is bigger than 1
    if i % 2 == 0:      # if statement to check if i is even (remainder 0)
        i = i // 2      # new value of i is calculated
        print(i)        # print new value of i
        continue        # continue - jump back to the start to check if if statement condition is met
    elif i % 2 == 1:    # elif statement to check if i is odd (remainde 1)
        i = ((i*3)+1)   # new value of is calculated
        print(i)        # print new value of i
        continue        # continue - jump back to the start to check if if statement condition is met
    elif i == 1:        # elif - condition when i equals 1 the probram should stop
        break           # stop further checks in the loop; 
                        # while i > 1 is false the program stops
    
    