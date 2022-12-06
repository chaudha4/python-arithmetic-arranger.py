# https://adventofcode.com/2021/day/11

# https://github.com/hyper-neutrino/advent-of-code/blob/main/2021/day11p1.py

def parray(data):
    for ii in range(len(data)):
        print(data[ii]) 
    print()


def load(file="adventofcode/temp.txt"):

    data = []
    with open(file, "r") as f:
        row = f.read().split()
        for rr in row:
            # Create a two dim array of integers
            data.append(list(int(chr) for chr in rr))
    return data

def countFlash(data):
    count = 0
    ii, jj = 0, 0
    for ii in range(len(data)):
        for jj in range(len(data[ii])):
            if (data[ii][jj] == 0):
                count = count + 1

    return count

def allFlashSimultaneously(data):

    for ii in range(len(data)):
        for jj in range(len(data[ii])):
            if (data[ii][jj] != 0):
                return False

    return True


def resetFlashed(data):

    for ii in range(len(data)):
        for jj in range(len(data[ii])):
            if (data[ii][jj] == -1):
                data[ii][jj] = 0

    return data



def evaluateEnergyLevel(data, steps=1):

    newdata = data
    count = 0
    for step in range(steps):
        print(f"\nIn Step {step+1}")

        # Those with energy level 10 or more will flash. This will cause energy
        # level to spike for adjacent cells. So need to do this recursively.
       
        newdata = flashRecursively(newdata)
        count = count + countFlash(newdata)
        parray(newdata)

    return count

def flashRecursively(data):
    ii, jj = 0, 0
    for ii in range(len(data)):
        for jj in range(len(data[ii])):
            data = flash(data, ii, jj)

    return resetFlashed(data)


# recursive
def flash(data, ii, jj):

    # Base Case - No Adjacent flashes left.
    tmp = data[ii][jj]

    # Already Flashed. Just return
    # An octopus can only flash at most once per step.
    if tmp == -1:
        return data

    # Simple case- No impact on adjacent cells.
    if tmp < 9:
        data[ii][jj] = data[ii][jj] + 1
        return data

    # Recursive case - any octopus with an energy level greater than 9 flashes. This increases 
    # the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent.

    # Set it to -1 to indicate that it has flashed to prevent double counting and then flash adjacents.
    data[ii][jj] = -1

    #left - Remember that -1 is a valid index in python. Will not throw an exception !!
    if (ii-1) > -1:
        data = flash(data, ii-1, jj)

    #right
    try:
        tmp = data[ii+1][jj]
        data = flash(data, ii+1, jj)
    except IndexError:
        pass

    #top
    if (jj-1) > -1:
        data = flash(data, ii, jj-1)

    #bottom
    try:
        tmp = data[ii][jj+1]
        data = flash(data, ii, jj+1)
    except IndexError:
        pass

    # diag top left
    if (jj-1) > -1 and (ii-1) > -1:
        data = flash(data, ii-1, jj-1)


    # diag top right
    try:
        if (jj-1) > -1:
            data = flash(data, ii+1, jj-1)
    except IndexError:
        pass

    try:
        tmp = data[ii+1][jj+1]
        data = flash(data, ii+1, jj+1)
    except IndexError:
        pass

    try:
        if (ii-1) > -1:
            data = flash(data, ii-1, jj+1)
    except IndexError:
        pass


    return data


def puzzle1():

    data = load("adventofcode/11-dumbo-octopus.txt")
    parray(data)
    steps = 100
    print(f'After step {steps}, there have been a total of {evaluateEnergyLevel(data, steps)} flashes.')

def puzzle2():
    newdata = load("adventofcode/11-dumbo-octopus.txt")
    #newdata = load()
    allFlashed = False
    steps = 0

    while (allFlashed == False):      
        newdata = flashRecursively(newdata)
        if allFlashSimultaneously(newdata):
            allFlashed = True
        steps = steps + 1
    
    print(f'The first step during which all octopuses flash is {steps}')



fcnt = 0
allFlashed = False

def step(data, look4allflashed = False):
    for r in range(0, len(data)):
        for c in range(0, len(data[r])):
            data[r][c] += 1
            if data[r][c] == 10:
                flash(data, r, c)
    
    if (look4allflashed):
        global allFlashed
        allFlashed = True
        for r in range(0, len(data)):
            for c in range(0, len(data[r])):
                if data[r][c] < 10:
                    allFlashed = False
                    break
    

    #Reset to zero for all the octopuses that flashed.
    for r in range(0, len(data)):
        for c in range(0, len(data[r])):
            if data[r][c] > 9:
                data[r][c] = 0
    
        

def flash(data, r, c):
    global fcnt
    fcnt += 1
    
    # handle the adjacent cells
    for x in range(r-1, r+2):
        for y in range(c-1, c+2):
            # Only process the adjacent cells.
            if (x == r and y == c):
                continue
            
            # Watch out for out of range cells.
            if (0 <= x < len(data)) and (0 <= y < len(data[0])):
                data[x][y] += 1
                if data[x][y] == 10:
                    flash(data, x, y)
                    
                    



def puzzle1a():
    data = load("adventofcode/11-dumbo-octopus.txt")
    #data = load()
    parray(data)
    for i in range(100):
        print(f'In step {i} -----------')
        step(data)
        parray(data)
    
    print(fcnt)


def puzzle2a():
    data = load("adventofcode/11-dumbo-octopus.txt")
    #data = load()
    #parray(data)

    stp = 1
    while True:
        #print(f'In step {i} -----------')
        step(data, True)
        if allFlashed:
            print(stp)
            break

        stp += 1
        #parray(data)
    
    print(fcnt)


#puzzle1()
#puzzle2()
puzzle2a()