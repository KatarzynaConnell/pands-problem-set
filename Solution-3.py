# Kasia Connell, 2019
# Solution to question 3
# The program will print all the numbers between 1,000 and 10,000 that are divisible by 6 but not by 12

# References: Ian's video tutorials: https://web.microsoftstream.com/video/20963781-2aea-4302-ba73-5b8f327f4189
# References: Ian's video tutorials: https://web.microsoftstream.com/video/82894055-5147-487d-ab35-6bf5c51cd889

# establish the range of numbers to be checked
for x in range(1000, 10001):        
    if ( x % 6 == 0) and (x % 12 != 0):     # set condition: if x divided by 6 leaves no remainded and x divided by 12 leaves a remainder
        print (x)                           # print the number