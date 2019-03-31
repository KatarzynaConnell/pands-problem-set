# Kasia Connell, 2019
# Solution to Question 10
# The Program will output the plot of functions x, power x and 2 to the power of x in the range [0,4]
# References:
# Video tutorial about Numpy: https://web.microsoftstream.com/video/74b18405-5ee1-47f0-a42d-e8831a453a91
# Video tutorial about plotting with Matplotlib: https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7

# Import numpy solution to analyze data
import numpy as np
# Import matplotlib to show data on the plot
import matplotlib.pyplot as pl
# set the range of x from 0 to 4
x = np.arange(0,5)

# list of the 3 functions required:
f1 = x
f2 = x**2
f3 = 2**x
    
# Set propertie of the line functions:    
# Adopted from https://matplotlib.org/users/pyplot_tutorial.html 
pl.plot(x, f1, 'r') # red line

pl.plot(x, f2, 'y') # yellow line

pl.plot(x, f3, 'k') # black line

# Graph names labels: Adopted from https://matplotlib.org/gallery/subplots_axes_and_figures/axes_demo.html 
pl.xlabel('X')
pl.ylabel('Y')
pl.title('x, power x and 2 to the power of x') 

# legend details
pl.legend(['f1 = x', 'f2 = x**2', 'f3 = 2**x'])

# Display grid lines
pl.grid(axis='both')

# display graph
pl.show()