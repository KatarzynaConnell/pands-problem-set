# Kasia Connell, 2019
# Solution to Question 10
# The Program will output the plot of functions x, power x and 2 to the power of x in the range [0,4]

import math
import numpy

x = int

for x in range(0,5):
    power1 = x**2
    power2 = 2**x
    print(x, power1, power2)
    continue
import matplotlib.pyplot as pl 
pl.plot([x])
pl.ylabel(power1)
pl.hist(x)
pl.show()

#pl.hist(power1)
#pl.show(power1)
#pl.hist(power2)
#pl.show(power2)