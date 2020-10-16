
from time import time

""" 
Retruns an array containing the fib sequence. This is a slow version since it
will redo same calculations on every run. Example fib(4) is done twice when 
fib(5) is called. A better implementation would be to cache this value rather
than recalculate it.
"""
def fib(n):

    # Utility function that calcualates the fib using recursion
    def calc_fib(n):
        if n == 0 or n == 1:
            return n
        else:
            ff = calc_fib(n-1) + calc_fib(n-2)
            return ff

    # Start from zero and calculate fib for each and save the result.
    res = []
    for ii in range(n):
        res.append(calc_fib(ii))
    
    # Return Result
    return res

"""
Better version.  Cache the resullts.
"""
def fib1(n):

    fib_val = {0:1, 1:1}    # cache

    # Utility function that calcualates the fib using recursion
    def calc_fib(n):
        try:
            return fib_val[n]
        except KeyError:
            # Not in cache. Calculate, save in cache and return
            ff = calc_fib(n-1) + calc_fib(n-2)
            fib_val[n] = ff
            return ff

    # Start from zero and calculate fib for each and save the result.
    res = []
    for ii in range(n):
        res.append(calc_fib(ii))
    
    # Return Result
    return res

""" 
Without recursion. This is actually the fastest and most efficient solution. Recursion is
not necessarily the best solution especially if there is chance that the same operiation
would be repeated.
"""

def fib2(n):

    ret = []

    for ii in range(n):
        if ii == 0 or ii == 1:
            ret.append(ii)
        else:
            ret.append(ret[ii-1] + ret[ii-2])
    
    return ret


# fib(100) takes a long time. Several minutes. So try fib(30) which takes about .6 sec.
before=time()
#print(fib(30))
after=time()
print("Time taken ", (after - before) *1000)

# fib1(100) takes .2 msecs !! Much Much Faster !!
before=time()
print(fib1(100))
after=time()
print("Time taken ", (after - before) *1000)

# fib2(100) takes .2 msecs !! Much Much Faster !!
before=time()
print(fib2(100))
after=time()
print("Time taken ", (after - before) *1000)
