"""

Do you know the difference between the following syntax?
[x for x in range(5)]
(x for x in range(5))
tuple(range(5))

See https://djangostars.com/blog/list-comprehensions-and-generator-expressions/

list reserves memory for the whole list and calculates it on the spot. In case of generator, we receive 
only ”algorithm”/ “instructions” how to calculate that Python stores. And each time we call for generator
, it will only “generate” the next element of the sequence on demand according to instructions.

"""

import sys

a = [x * 5 for x in range(100)]
b = (x * 5 for x in range(100))
c = tuple(x * 5 for x in range(100))

print( sys.getsizeof(a) )    # Prints 9016
print( sys.getsizeof(b) )    # Print 112
print( sys.getsizeof(c) )    # Print 840

print(a)
print(b)
print(c)