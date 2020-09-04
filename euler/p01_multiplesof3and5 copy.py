""" 
Project Euler: Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided parameter value number. 

"""

def multiples(n):
    sum = 0
    for ii in range(n):
        if (ii % 3 == 0 or ii % 5 == 0):
            sum += ii
    return sum



def testme():

    assert multiples(10) == 23, "Sum of all multiples in 3,5 for 0 to 10 should be 23"




if __name__ == "__main__":
    testme()
    print("*" * 50, "Everything passed. No asserts if we reached here", "*" * 50, sep="\n")