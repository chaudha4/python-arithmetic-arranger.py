
"""  
Write a program that prints the numbers from 1 to 100. 
For numbers which are multiples of both three and five print “FizzBuzz” 
"""

def fizz_buzz1():
    ret = []
    for ii in range(1,101):
        if ii % 3 == 0 and ii % 5 == 0:
            ret.append("FizzBuzz")
        else:
            ret.append(ii)
    return ret


"""  
Write a program that accepts a list of integers and mutates it
for numbers which are multiples of both three and five with “FizzBuzz” 
"""

# using range to track index
def fizz_buzz2(numbers):
    for ii in range(len(numbers)):
        if numbers[ii] % 3 == 0 and numbers[ii] % 5 == 0:
            #breakpoint()
            numbers[ii] = "FizzBuzz"


# using enumerate to track index
def fizz_buzz3(numbers):
    for index, num in enumerate(numbers):
        if num % 3 == 0 and num % 5 == 0:
            numbers[index] = "FizzBuzz"




if __name__ == "__main__":
    
    #print(fizz_buzz1())

    numbers = [1,5,15,20]
    fizz_buzz2(numbers)
    print(numbers)


    numbers = [1,5,15,20]
    fizz_buzz3(numbers)
    print(numbers)