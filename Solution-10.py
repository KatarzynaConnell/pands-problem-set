# Kasia Connell, 2019
# Solution to Question 10
# The Program will output the plot of functions x, power x and 2 to the power of x in the range [0,4]

#Imort math solution 
import math
#Import numpy solution for the purpose of plot
import numpy
# set the range of x from 0 to 4
x = range(0,5)

# to calculate the power of x:
for x in range(0,5): 
    f1 = x**2
#to calculate 2 to the power of x:
    f2= 2**x
    print(x, f1, f2)  # Print all the value of x, x to the powoer of 2, 2 to the power of x
    
# import matplot pyplot and assign it name pl
import matplotlib.pyplot as pl  
# for the plot to be created enter:
pl.hist(x)  # command to create the plot for value x
pl.show(x)  # command to show the plot for value x
 
pl.hist(f1) # command to create the plot for f1
pl.show(f1) # command to show the plot for f1

pl.hist(f2) # command to create the plot for f2
pl.show(f2) # command to show the plot for f2