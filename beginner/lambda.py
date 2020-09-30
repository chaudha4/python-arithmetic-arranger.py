
"""
Syntax
^^^^^^
lambda arguments : expression

"""

fx = lambda: print("This is lambda")
fx()

fx = lambda arg: print(f'This is {arg}')
fx("lambda")

# Variable Arguments (Positional)
fx = lambda *arg: print(f'This is {arg[0]}')
fx("lambda1", "lambda2")

# Variable Arguments (Key Value pairs)
fx = lambda **arg: print(f'This is {arg["key2"]}')
fx(key1="lambda1", key2="lambda2")


# Implicit return
fx = lambda k: k ** 2
print(fx(10))   # 100

# Implicit return dict
fx = lambda k, v : {k:v}
d1 = fx("key", "value")
print(d1)
print(type(d1)) # <class 'dict'>

# Implicit return set
fx = lambda k, v : {k, v}
d1 = fx("key", "value")
print(d1)
print(type(d1)) # <class 'set'>

print(type(fx)) # <class 'function'>

# Both do same thing - One is a pythonic way !! - https://realpython.com/python-lambda/#alternatives-to-lambdas
print(list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow'])))
print([x.capitalize() for x in ['cat', 'dog', 'cow']])

# Examples of Default arguments
fx = lambda v, k="Key" : {k: v}
print(fx(10))           # {'Key': 10}
print(fx(10, "myKey"))  # {'myKey': 10}


# Variable list of arguments
fx = lambda *args : max(args)
print(fx(1,2,3,4))