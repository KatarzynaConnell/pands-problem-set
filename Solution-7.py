# Kasia Connell, 2019
# Solution to Question 7
# The program will ask to input a positive floating point number and will output approximation of its square root.

# References:
# Ian's video tutorial: https://web.microsoftstream.com/video/dca7ddaa-9512-4810-a758-237921e6440e


# the number to calculate the square root of
rootof = 123456.0
# The initial prediction for the square root
prediction = 6

# Keep counting until the square of estimate is within 0.1 of rootof
while abs((prediction * prediction) -rootof) > 0.1:
# As per Newton's method how to improve the estimate
# Adapted from https://tour.golang.org/flowcontrol/1
prediction -= (prediction * prediction) - rootof) / (2*prediction)

# Print the result
print(f"the square root of {rootof} is approx. {prediction}.")
