
"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n
"""

def test(N, n):
    """
    >>> test(8, 2)
    True
    >>> test(8, 3)
    False
    >>> test(24, 4)
    True
    """

    for ii in range(n,0,-1):    # Start from n and down till 1
        if (N%ii > 0):
            return False
    return True

def solution(N):
    """
    >>> solution(5)
    60
    >>> solution(7)
    420
    >>> solution(10)
    2520
    >>> solution(13)
    360360
    >>> solution(20)
    232792560        
    """    
    ret = N
    n = N
    while(test(ret, n) == False):
        ret += 1
    return ret


if __name__ == "__main__":
    import doctest  # See https://docs.python.org/3/library/doctest.html
    doctest.testmod(verbose=True)      



