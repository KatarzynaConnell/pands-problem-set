# Kasia Connell, 2019
# Solution to Question 10
# The Program will output the plot of functions x, power x and 2 to the power of x in the range [0,4]

#Import numpy solution for the purpose of plot
import numpy as np
#Import matplotlib to show data on the plot
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

# Graph names 
pl.xlabel('X')
pl.ylabel('Y')
pl.title('x, power x and 2 to the power of x') 

#Legend details

pl.legend(['f1 = x', 'f2 = x^2', 'f3 = 2^x'])


#Show grid lines

pl.grid(axis='both')

#display graph

pl.show()