

def count_ones(N):
    """
    Count number of ones in a binary representation of a given decimal N
    >>> count_ones(8)
    1
    >>> count_ones(9)
    2
    >>> count_ones(7)
    3
    """

    num = 0

    while(N>0):
        if (N & 1) == 1:
            num += 1
        N = N >> 1
    
    return num


def convert_to_binary(N):
    """
    Count number of ones in a binary representation of a given decimal N
    >>> convert_to_binary(8)
    '1000'
    >>> convert_to_binary(9)
    '1001'
    >>> convert_to_binary(7)
    '111'
    """

    bin_arr = ""

    # You can also use builtin function bin(N)
    while (N > 0):
        bin_arr += str(N%2)
        N = N // 2

    return bin_arr[::-1]    # Reverse the string

   


if __name__ == "__main__":
    import doctest  # See https://docs.python.org/3/library/doctest.html
    doctest.testmod(verbose=True)  