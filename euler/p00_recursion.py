"""
Recursion is "bad" in Python because it is usually slower than an iterative solution, and because 
Python's stack depth is not unlimited and there's no tail call optimization.
"""

from time import time

def factorial1(n):
    if n == 1:
        return n
    else:
        return (n * factorial1(n-1))


def factorial2(n):
    ret = 1
    while n > 0:
        ret = ret * n
        n = n - 1
    return ret


#print(factorial1(4))
#print(factorial2(4))

before=time()
factorial1(200) # This will fail at 1000 - You get - RecursionError: maximum recursion depth exceeded in comparison
after=time()
print("Time taken for factorial1", (after - before) *1000)

before=time()
factorial2(200)
after=time()
print("Time taken for factorial2", (after - before) *1000)


# Recursion is slower and could run out of stack space.
# Time taken for factorial1 0.2460479736328125
# Time taken for factorial2 0.0331401824951171