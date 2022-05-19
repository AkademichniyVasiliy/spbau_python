from numba import jit
import time

def combinations (n, k):
    if n < 0 or k < 0:
        return 0
    if n < k:
        return 0 
    if n == k:
        return 1
    return combinations(n-1, k) + combinations(n-1, k-1)

@jit(nopython=True)
def combinations_jit(n, k):
    if n < 0 or k < 0:
        return 0
    if n < k:
        return 0 
    if n == k:
        return 1
    return combinations_jit(n-1, k) + combinations_jit(n-1, k-1)

n, k = 25, 15
start_time = time.time()
print(f'{n} choose {k} is {combinations_jit(n,k)}, Executed with jit in: {time.time()-start_time} seconds')
start_time = time.time()
print(f'{n} choose {k} is {combinations(n,k)}, Executed without jit in: {time.time()-start_time} seconds')
print('Massive difference huh')
