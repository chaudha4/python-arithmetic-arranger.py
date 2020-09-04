
# https://docs.python-guide.org/writing/style/


def isoddv1(n):
    """
    Is odd number
    >>> isoddv1(3)
    True
    """

    return not n % 2 == 0   # Reminder should not be zero for an odd number

def isoddv2(n):
    """
    Is odd number - Another way
    >>> isoddv2(5)
    True
    """

    return n & 1 == 1   # Last bit is 1 for odd number


def reverse_array(n):
    """
    Reverse an array (or string). If it is string, you can also use the reverse() method.
    >>> reverse_array([1,2,3])
    [3, 2, 1]

    This works for String too !!
    >>> reverse_array("abhishek")
    'kehsihba'

    """    
    return n[::-1]

def get_nth_digit(N, n):
    """
    return the nth digit from an N digit number 
    >>> get_nth_digit(12345, 3)
    4
    >>> get_nth_digit(12345, 7)
    Traceback (most recent call last):
    ...
    IndexError: string index out of range
    """

    return int(str(N)[n])


def split(n):
    """
    Split string or Array
    >>> split("hello")
    ['he', 'llo']
    >>> split([1,2,3,1,2,4])
    [[1, 2, 3], [1, 2, 4]]
    """    
    return [ n[:len(n)//2:], n[len(n)//2::] ]

def is_anagram(a, b):
    """
    Checking if two words are anagrams
    >>> is_anagram("hello", "helol")
    True
    >>> is_anagram("hello", "helllo")
    False
    """  

    return sorted(a) == sorted(b)

def contains_pattern(str, pat):
    """
    Checking if pat is in str
    >>> contains_pattern("hello", "lo")
    True
    >>> contains_pattern("hello", "ol")
    False
    >>> contains_pattern([1,2,3,4,5], 4)
    True
    >>> contains_pattern([1,2,3,4,5], 6)
    False
    """ 

    return str.count(pat) > 0

def remove_duplicates(a):
    """
    Remove Duplicates from an Array
    >>> sorted(remove_duplicates("hello"))
    ['e', 'h', 'l', 'o']
    >>> remove_duplicates([1,2,3,1,2,4])
    [1, 2, 3, 4]
    """  
      
    return list(set(a))




# Find min in an array
def findmin(n):
    ret1 = min(n)    # Option 1 - built in function

    # Option 2 - loop
    ret2 = n[0]
    for val in n:
        if val < ret2:
            ret2 = val

    # Option 3 - loop with enumerate on index, value
    ret3 = n[0]
    for _, val in enumerate(n):
        if val < ret3:
            ret3 = val            

    print(ret1, ret2, ret3)

    return ret1



if __name__ == "__main__":

    import doctest  # See https://docs.python.org/3/library/doctest.html
    doctest.testmod(verbose=False)    