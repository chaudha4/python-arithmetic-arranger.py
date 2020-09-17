"""
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.
"""

def solution(n):
    """
    >>> solution(10)
    2640
    >>> solution(20)
    41230
    >>> solution(100)
    25164150
    """
    a = sum([x**2 for x in range(n+1)])
    b = sum([x for x in range(n+1)]) ** 2
    return b-a



if __name__ == "__main__":
    import doctest  # See https://docs.python.org/3/library/doctest.html
    doctest.testmod(verbose=True)      



