from math import *

def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)

print f(10.,4.,10.) #Change the 8. to something else!

def update(mean1, var1, mean2, var2):
    return [1 / (var1 + var2) * (var2 * mean1 + var1 * mean2) , 1 / (1 / var1 + 1 / var2)]

def predict(mean1, var1, mean2, var2):
    addition = update(mean1, var1, mean2, var2)
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

print update(10., 4., 12., 4.)
print update(10., 8., 13., 2.)
print predict(10., 4., 12., 4.)
print "-----------------------------------"
measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for i in range(len(measurements)):
    [mu,sig] = update(mu,sig,measurements[i],measurement_sig)
    print 'update: ', [mu,sig]
    [mu, sig] = predict(mu,sig,motion[i],motion_sig)
    print 'predict: ', [mu, sig]
print [mu, sig]