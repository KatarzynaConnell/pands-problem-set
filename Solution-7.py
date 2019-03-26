# Kasia Connell, 2019
# Solution to Question 7
# The program will ask to input a positive floating point number and will output approximation of its square root.

# References:
# Ian's video tutorial: https://web.microsoftstream.com/video/dca7ddaa-9512-4810-a758-237921e6440e


# the number to calculate the square root of
rootof = 98765.0
# The initial estimation for the square root
estimate = 320

# Using absolute value keep counting until the square of estimate is within 0.1 of rootof
while abs((estimate * estimate) - rootof) > 0.1:
# As per Newton's method how to improve the estimate
# Adapted from https://tour.golang.org/flowcontrol/1
    estimate -= ((estimate * estimate) - rootof) / (2 * estimate)

# Print the result
print(f"the square root of {rootof} is approx. {estimate}.")
