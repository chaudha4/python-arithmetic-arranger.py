
"""
Ask the user for a number and determine whether the number is prime or not.
"""

def isprime(a):
    for aa in range(2,a):
        if (a % aa) == 0:
            print("Not a prime - ", a)
            return False
    return True


num = input("Please enter a number" + "\n" + ">>>")

if isprime(int(num)):
    print(f"The number {num} is prime")
else:
    print(f"The number {num} is not a prime")