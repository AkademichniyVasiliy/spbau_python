from numpy import exp
from numba import jit 
from random import uniform
import time

# *** integrating e^(-x^2) on [-25, 25) ***

def integral(samples, points_per_sample):     
    total = 0
    for i in range(samples):
        summa = 0 
        for j in range(points_per_sample):
            x = uniform(-25, 25)
            fx = exp(-(x**2))   
            summa += fx
        total += summa*50/points_per_sample
    return total/samples

@jit(nopython = True)
def integral_jit(samples, points_per_sample):     
    total = 0
    for i in range(samples):
        summa = 0 
        for j in range(points_per_sample):
            x = uniform(-25, 25)
            fx = exp(-(x**2))   
            summa += fx
        total += summa*50/points_per_sample
    return total/samples

start_time = time.time()
value_jit = integral_jit(2000, 10_000)   # 2000 integrals calculated, 10_000 points evaluated per integral
time_jit = time.time() - start_time
print(f'The integral of e^(-x^2) on [25; 25) is approximately {value_jit}, execution time with jit: {time_jit}')

start_time = time.time()
value_no_jit = integral(2000, 10_000)
time_no_jit = time.time() - start_time
print(f'The integral of e^(-x^2) on [25; 25) is approximately {value_no_jit}, execution time without jit: {time_no_jit}')
print(f'Now THAT is massive difference: {time_no_jit/time_jit} times. Will Google hire me for using this dark magic?')

# ***Side note: for samples, points_per_sample = 10_000, 30_000, the difference is about 7s against 391s, 56 times