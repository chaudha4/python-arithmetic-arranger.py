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
    st = str(n)
    return st == st[::-1]

def largest(n):
    lnum = int("9" * n)
    rnum = lnum
    lp = -1

    for ii in range(rnum + 1):
        for jj in range(lnum + 1):
            kk = ii * jj
            if (ispalindrome1(kk) and kk > lp ):
                lp = kk


    return lp


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
    testme()
    print("Everything passed. No asserts if we reached here")





