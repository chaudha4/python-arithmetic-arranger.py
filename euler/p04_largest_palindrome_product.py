"""
A palindromic number reads the same both ways. The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99.
"""

def ispalindrome(n):
    st = str(n)
    ll = len(st)
    for ii in range(ll // 2):
        if (st[ii] != st[ll-ii-1]):
            return False
    return True

def ispalindrome1(n):
    """
    Will work for string and numbers
    >>> ispalindrome1("hello")
    False
    >>> ispalindrome1("SOS")
    True
    >>> ispalindrome1(123)
    False
    >>> ispalindrome1(121)
    True
    """        
    st = str(n)
    return st == st[::-1]

def largest(n):
    """
    Will work for string and numbers
    >>> largest(2)
    9009
    >>> largest(3)
    906609
    """         
    lnum = int("9" * n)                     # largest n digit number
    snum = int( "9" * (n - 1) ) + 1         # Smallest n digit number

    #print(lnum, snum)

    rnum = lnum
    lp = -1

    # Brute Force Method. O(N^2). Takes hours on 5 digit number
    
    for ii in range(snum, rnum + 1):
        for jj in range(snum, lnum + 1):
            kk = ii * jj
            if (ispalindrome1(kk) and kk > lp ):
                lp = kk
       

    return lp


def largest_v2(n):
    """
    Will work for string and numbers
    >>> largest_v2(2)
    9009
    >>> largest_v2(3)
    906609
    >>> largest_v2(4)
    99000099
    >>> largest_v2(5)
    99000099    
    """         
    lnum = int("9" * n)                  # largest n digit number
    snum = int( "9" * (n - 1) )          # largest n-1 digit number

    # Brute Force Method. O(N^2). Go from largest to half way. That shoudld help !!
    
    ge = (ii * jj for ii in range(lnum, snum, -1) for jj in range(lnum, snum, -1))
    products = sorted(set(ge))  # duplicates removed and sorted.
    
    
    for ii in range(len(products) - 1, -1, -1):
        
        if (ispalindrome1(products[ii])):
            return products[ii]

    return -1


def testme():
    assert type(largest(2)) == int, "largest() should retun an int type"
    assert ispalindrome(1), "ispalindrome(1) should be True"
    assert ispalindrome(12) == False, "ispalindrome(1) should be False"
    assert ispalindrome(11), "ispalindrome(11) should be True"
    assert ispalindrome(121), "ispalindrome(1) should be True"
    assert ispalindrome(122) == False, "ispalindrome(122) should be False"
    assert largest(2) == 9009, "largest palindrome made from the product of two 2-digit numbers should return 9009"
    assert largest(3) == 906609, "largest palindrome made from the product of two 3-digit numbers should return 906609"


if __name__ == "__main__":
    #testme()
    #print("Everything passed. No asserts if we reached here")

    import doctest  # See https://docs.python.org/3/library/doctest.html
    doctest.testmod(verbose=False)      





