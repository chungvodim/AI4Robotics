from math import *

def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)

print f(10.,4.,10.) #Change the 8. to something else!

def update(mean1, var1, mean2, var2):
    return [1 / (var1 + var2) * (var2 * mean1 + var1 * mean2) , 1 / (1 / var1 + 1 / var2)]
print update(10., 4., 12., 4.)
print update(10., 8., 13., 2.)