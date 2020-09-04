

""" 
The prime factors of 13195 are 5, 7, 13 and 29. The largest one is 29.

"""

def largest_prime_factor(n):

    ret = None

    for ii in range(3, n + 1):
        if (n % ii == 0):
            if is_prime(ii):
                ret = ii

    return ret

def is_prime(n):
    for ii in range(2, n // 2):     # If num is divisible by any number between 2 and n / 2, it is not prime
        if (n % ii == 0):
            return False
    return True

print(largest_prime_factor(13195))
print(largest_prime_factor(14))