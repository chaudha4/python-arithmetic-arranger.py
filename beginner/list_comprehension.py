print(f"\n{'*' * 50}")
# Example 1 - Using Square function

def square(x):
    return x * x

print(f'Square of 5 is {square(5)}')

lst = [1, 2, -5, 4]

# Apply the square function to each element in the list - Using For loop

rslt = list() # Or rslt = []

for ii in lst:
    rslt.append(square(ii))
print("Example 1 - Using Loop", rslt)

# Apply the square function to each element in the list - Using Map (Python discourages use of map, filter)
mp = map(square, lst)
print("Example 1 - Using Map", list(mp))

# Apply the square function to each element in the list - Using list comprehension (Pythonic Way - Preferred)
rslt = [square(x) for x in lst]
print("Example 1 - Using list comprehension", rslt)

print(f"\n{'*' * 50}")

# Example 2 - Filter odd numbers from a list

def is_odd(num):
    return num % 2 == 1

lst = [1, 2, 4, 6, 3, 9]

# Using for loop
rslt = []
for ii in lst:
    if is_odd(ii):
        rslt.append(ii)
print("Example 2 - Using Loop", rslt)

# using filter
rslt = list(filter(is_odd, lst))
print("Example 2 - Using Filter", rslt)

# using list comprehension
rslt = [ii for ii in lst if is_odd(ii)]
print("Example 2 - Using list comprehension", rslt)

print(f"\n{'*' * 50}")

# Example 3 - Create a grid of r rows and c columns

def create_grid(rows, cols):
    grid = []
    for _ in range(rows):       # The underscore is also used for ignoring the specific values so linter does not complain
        row = []
        for _ in range(cols):
            row.append(0)
        grid.append(row)
    return grid

print("Example 3 - Using Loop", create_grid(3,4))

def create_grid1(rows, cols):
    return [ [0 for c in range(cols)] for r in range(rows)  ]

print("Example 3 - Using list comprehension", create_grid1(3,4))



