"""
You are given two arrays A and B consisting of N integers each.

Index K is named fair if the four sums (A[0] + ... + A[K-1]), (A[K] + ... + A[N-1]), (B[0] + ... + B[K-1]) and 
(B[K] + ... + B[N-1]) are all equal. In other words, K is the index where the two arrays, A and B, can be split 
(into two non-empty arrays each) in such a way that the sums of the resulting arrays' elements are equal.

For example, given arrays A = [0, 4, -1, 0, 3] and B = [0, -2, 5, 0, 3], index K = 3 is fair. The sums of the 
subarrays are all equal: 0 + 4 + (-1) = 3; 0 + 3 = 3; 0+(-2) + 5 = 3 and 0 + 3 = 3. On the other hand, index 
K = 2 is not fair; the sums of the subarrays are: 0 + 4 = 4; (-1) + 0 + 3 = 2; 0+(-2) = -2 and 5 + 0 + 3 = 8.


Examples:

1. Given A = [0, 4, -1, 0, 3] and B = [0, -2, 5, 0, 3], your function should return 2. The fair indexes are 3 and 4. 
In both cases, the sums of elements of the subarrays are equal to 3.

2. Given A = [2, -2, -3, 3] and B = [0, 0, 4, -4], your function should return 1. The only fair index is 2. 
Index 4 is not fair as the subarrays containing indexes from K to N - 1 would be empty.

3. Given A = [4, -1, 0, 3] and B = [-2, 6, 0, 4], your function should return 0. There are no fair indexes.

4. Given A = [3, 2, 6] and B = [4, 1, 6], your function should return 0.

5. Given A = [1, 4, 2, -2, 5], B = [7, -2, -2, 2, 5], your function should return 2. The fair indexes are 2 and 4.
"""

def fair_split(A, B):
    """
    >>> fair_split([0, 4, -1, 0, 3], [0, -2, 5, 0, 3])
    2
    >>> fair_split([2, -2, -3, 3], [0, 0, 4, -4])
    1
    >>> fair_split([3, 2, 6],[4, 1, 6])
    0
    >>> fair_split([1, 4, 2, -2, 5], [7, -2, -2, 2, 5])
    2
    """

    fair_count = 0

    for ii in range(1,len(A)):
        #print(ii, sum(A[:ii]), sum(A[ii::]), sum(B[:ii]), sum(B[ii::]))
        if ( sum(A[:ii]) == sum(A[ii::]) == sum(B[:ii]) == sum(B[ii::] ) ):
                fair_count += 1

    return fair_count

if __name__ == "__main__":
    #print(fair_split([0, 4, -1, 0, 3], [0, -2, 5, 0, 3]))
    #print(fair_split([2, -2, -3, 3], [0, 0, 4, -4]))
    #print(fair_split([3, 2, 6],[4, 1, 6]))

    import doctest  # See https://docs.python.org/3/library/doctest.html
    doctest.testmod(verbose=True)      