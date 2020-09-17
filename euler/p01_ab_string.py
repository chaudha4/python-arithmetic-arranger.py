"""
Write a function solution that, given a string S consisting of N letters 'a' and/or 'b' returns True when all occurrences of letter 'a' are 
before all occurrences of letter 'b' and returns False otherwise.

Examples:

1. Given S = "aabbb", the function should return True.

2. Given S = "ba", the function should return False.

3. Given S = "aaa", the function should return True. Note that 'b' does not need to occur in S.

4. Given S = "b", the function should return True. Note that 'a' does not need to occur in S.

5. Given S = "abba", the function should return False.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..300,000];
string S consists only of the characters 'a' and/or 'b'.

"""

def ab_string(S):

    """
    >>> ab_string("aaaaaaabbbbbbbbbb")
    True
    >>> ab_string("b")
    True
    >>> ab_string("aba")
    False
    >>> ab_string("aaba")
    False
    """

    found_b = False
    for aa in S:
        if ( aa == "b"):
            found_b = True
        else:
            # must be a
            if (found_b):
                return False
    
    return True

def ab_string_v2(S):

    """
    >>> ab_string("aaaaaaabbbbbbbbbb")
    True
    >>> ab_string("b")
    True
    >>> ab_string("aba")
    False
    >>> ab_string("aaba")
    False
    """

    if S.indexof("ba") == -1:
        return True
    return False

def ab_string_v3(S):

    """
    >>> ab_string("aaaaaaabbbbbbbbbb")
    True
    >>> ab_string("b")
    True
    >>> ab_string("aba")
    False
    >>> ab_string("aaba")
    False
    """

    if len(S.split("ba")) == 1:
        return False
    return True


if __name__ == "__main__":
    import doctest  # See https://docs.python.org/3/library/doctest.html
    doctest.testmod(verbose=True)  