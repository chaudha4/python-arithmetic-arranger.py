"""
Fibonacci Sequence
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

"""

"""
Using for loop only
"""

def fib1(n):
    ret = [1]
    prev = 0
    prev1 = 1
    for aa in range(n-1):
        val = prev + prev1
        ret.append(val)
        prev = prev1
        prev1 = val
    
    print(ret)

    return ret

"""
Using Index shortcut
"""

def fib2(n):

    ret = [1]
    if (n==1):
        return ret

    for aa in range(1,n):
        ret.append(sum(ret[-2::]))

    print(ret)

    return ret




fib1(4)
fib2(4)