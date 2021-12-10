import numpy as np
from numpy.core.defchararray import rstrip


def get_low_points(file="adventofcode/temp.txt"):

    data = np.genfromtxt(file, delimiter=1)

    rows, cols = data.shape

    # Low points and Risk Level
    lp = []
    rl = []


    for row in range(rows):
        for col in range(cols):
            td = data[row, col]
            
            # up, down, left, right is smaller
            up,down,left,right = False,False,False,False

            if row in (0, rows-1):
                if (row == 0):
                    up = True
                else:
                    down = True    
                
                if col == 0:
                    left = True
                if col == cols - 1:
                    right = True

            if col in (0, cols-1):
                if (col == 0):
                    left = True
                else:
                    right = True    


            # Check Up
            if (up == False and td < data[row-1 , col]):
                up = True
            
            # Check Down
            if (down == False and td < data[row+1 , col]):
                down = True

            # Check left
            if (left == False and td < data[row , col - 1]):
                left = True

            # Check Down
            if (right == False and td < data[row , col + 1]):
                right = True
            
            if (left and right and up and down):
                lp.append((row,col))
                rl.append(td+1)

    return rl, lp


def get_basin(file="adventofcode/temp.txt"):

    data = np.genfromtxt(file, delimiter=1)

    rows, cols = data.shape

    rl, lp = get_low_points(file)

    for row, col in lp:
        print("Low Point is: ", data[row, col], ", X Y: ",row, col)

        rslt = get_higher_neighbours(data, [(row, col)])
        print(len(set(rslt)))


# recursive function !!
def get_higher_neighbours(data, input):

    #print("Entering with ", input)
    rslt = []
    for row, col in input:

        # up, down, left, right should be ignored
        up,down,left,right = False,False,False,False
        rows, cols = data.shape
        td = data[row, col]

        if row in (0, rows-1):
            if (row == 0):
                up = True
            else:
                down = True    
            
            if col == 0:
                left = True
            if col == cols - 1:
                right = True

        if col in (0, cols-1):
            if (col == 0):
                left = True
            else:
                right = True    


        # Check Up
        if (up == False):
            tocmp = data[row-1 , col]
            if(tocmp != 9 and td < tocmp ):
                rslt.append((row-1, col))

        # Check Down
        if (down == False):
            tocmp = data[row+1 , col]
            if (tocmp != 9 and td < tocmp ):
                rslt.append((row+1, col))

        # Check left
        if (left == False):
            tocmp = data[row , col-1]    
            if (tocmp != 9 and td < tocmp):
                rslt.append((row, col-1))

        # Check Down
        if (right == False):
            tocmp = data[row , col+1]
            if (tocmp != 9 and td < tocmp):
                rslt.append((row, col+1))


    # Recursion - Base case
    if len(rslt) == 0:
        # Return the input back so the it gets accumulated by the recursive case.
        return input
    
    # Recursion - Recursive case - Accumulate the data
    for data in get_higher_neighbours(data, rslt):
        input.append(data)
    return input
    

#Test
rl, lp = get_low_points()
print(sum(rl))

#Puzzle 1
rl, lp = get_low_points("adventofcode/09-smoke-basin.txt")
print(sum(rl))

#Puzzle 2
get_basin("adventofcode/09-smoke-basin.txt")