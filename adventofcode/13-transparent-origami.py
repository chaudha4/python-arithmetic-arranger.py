# https://adventofcode.com/2021/day/13
# https://youtu.be/cXSRh2PS9W0


def load(file="adventofcode/temp.txt") -> tuple():

    coordinates = set()
    folds = [] # maintain order or intructions

    with open(file, "r") as f:
        x_y, foldInstructions = f.read().split("\n\n")

        for rr in x_y.split("\n"):
            x, y = rr.split(",")    # Remember x,y are parsed as string chars !!
            coordinates.add((int(x), int(y)))

        for rr in foldInstructions.split("\n"):
            commnd, val = rr.split("=")
            folds.append([commnd[-1], int(val)])


    #print(coordinates)  # {(388, 374), (350, 518)}
    #print(folds)        # [['x', 655], ['y', 447]]
            
    return coordinates, folds

def printPaper(coordinates):
    #Find max x and y
    max_x = max(cc[0] for cc in coordinates) + 1
    max_y = max(cc[1] for cc in coordinates) + 1
    #print(f'Max Values are {max_x},{max_y}')

    print(f'Graph of size {max_x} X {max_y}')
    for y in range(max_y):
        for x in range(max_x):
            if (x,y) in coordinates:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    
    print()

def foldPaper(coordinates, fold):
    newc = set()
       
    if fold[0] == "x": # fold up along the horizontal line
        for x, y in coordinates:
            if x > fold[1]:
                moveby = x - fold[1]
                newx = fold[1] - moveby
                newc.add((newx,y))
            else:
                newc.add((x,y))
    else: # fold left along the vertical line
        for x, y in coordinates:
            if y > fold[1]:
                moveby = y - fold[1]
                newy = fold[1] - moveby
                newc.add((x,newy))
            else:
                newc.add((x,y))

    return newc


def foldPaper1(coordinates, folds):
    
    for fold in folds:
        newc = set()
        if fold[0] == "x": # fold up along the horizontal line
            for x, y in coordinates:
                if x > fold[1]:
                    moveby = x - fold[1]
                    newx = fold[1] - moveby
                    newc.add((newx,y))
                else:
                    newc.add((x,y))
            coordinates = newc
        else: # fold left along the vertical line
            for x, y in coordinates:
                if y > fold[1]:
                    moveby = y - fold[1]
                    newy = fold[1] - moveby
                    newc.add((x,newy))
                else:
                    newc.add((x,y))
        coordinates = newc

    return coordinates

def foldPaperUsingSetComprehension(coordinates, folds):
    
    for fold in folds:
        if fold[0] == "x": # fold up along the horizontal line

            # Using Comprenhension allows updating set while iterating it. This was not possible
            # with the previos method.
            coordinates = {
                (
                    x if x < fold[1] else fold[1] - (x - fold[1]),
                    y,
                )
                for x, y in coordinates
            }

        else: # fold left along the vertical line

            coordinates = {
                (
                    x,
                    y if y < fold[1] else fold[1] - (y - fold[1]),
                )
                for x, y in coordinates
            }

    return coordinates




def puzzle1():
    coordinates, folds = load("adventofcode/13-transparent-origami.txt")

    for ff in folds:
        coordinates = foldPaper(coordinates, ff)
    
    printPaper(coordinates)

def puzzle1a():
    coordinates, folds = load("adventofcode/13-transparent-origami.txt")

    coordinates = foldPaperUsingSetComprehension(coordinates, folds)
    
    printPaper(coordinates)

def puzzle1b():
    coordinates, folds = load("adventofcode/13-transparent-origami.txt")

    coordinates = foldPaper1(coordinates, folds)
    
    printPaper(coordinates)

puzzle1()
puzzle1a()
puzzle1b()