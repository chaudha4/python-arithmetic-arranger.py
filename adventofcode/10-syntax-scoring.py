#
# https://adventofcode.com/2021/day/10

def eliminateMatching(row):

    # convert to a list of chars from string
    line = list(row)

    print("Before:", line)

    valid_pair = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    

    for ii, cc in enumerate(line):

        #print("Processing, ", ii, cc)
        if cc == '':
            continue
        elif cc in valid_pair:
            #go reverse and look for match and clear both
            for jj in range(ii-1,-1,-1):
                if line[jj] == '':
                    continue
                elif line[jj] == valid_pair[cc]:
                    line[ii] = ''
                    line[jj] = ''
                    break
                else:
                    # Corrupt line. Return
                    return True, []
    

    print("After:", line)
    print("")
    return False, line

def getClosingChars(line):

    print("Finding closing pair for ", line)

    valid_pair = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    

    # iterate backwards
    closingList = []
    for cc in line[::-1]:
        if cc == '':
            continue
        else:
            closingList.append(valid_pair[cc])


    print(closingList)
    return closingList


def isCorruptedLine(row):

    line = list(row)
    
    valid = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    
    
    index = 0
    exp, fnd = '', ''
    #print(line)
    for ii, cc in enumerate(line):

        #print("Processing, ", ii, cc)
        if cc == '':
            continue
        elif cc in valid:
            index = ii
            #print("Valid Close detected at, ", ii, cc)
        
            #go reverse and look for match
            for jj in range(ii-1,-1,-1):
                if line[jj] == '':
                    continue
                elif line[jj] == valid[cc]:
                    line[ii] = ''
                    line[jj] = ''
                    break
                else:
                    print("This is a corrupted line - detected mismatch at index ", index, line[jj], cc)
                    return True, valid[cc], line[jj]
    
    return False, exp, fnd

def puzzle1(filename="adventofcode/temp.txt"):

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,    
        '(': 3,
        '[': 57,
        '{': 1197,
        '<': 25137,    

    }    

    with open(filename, "r") as f:
        data = f.read().split("\n")
        score = 0
        for row in data:
            rst, fnd, exp = isCorruptedLine(row)
            if (rst):
                print(row)
                print(f"Expected {exp}, but found {fnd}. Points received {points[fnd]}\n")
                score = score + points[fnd]

        print(f"The final score is {score}")


def puzzle2(filename="adventofcode/temp.txt"):

    valid_close = [")", "]", "}", ">"]

    with open(filename, "r") as f:
        data = f.read().split("\n")
        
        scores = []

        for row in data:
            corrupt, rr = eliminateMatching(row)
            if corrupt:
                continue
            else:
                clist = getClosingChars(rr)
                scores.append(getScore(clist))
        
        print(scores)

        sortedScores = sorted(scores)
        print(sortedScores[len(sortedScores) // 2])


def getScore(clist):

    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,    
    }        

    score = 0

    for cc in clist:
        score = (score * 5) + points[cc]
    
    print(f'The Score for {clist} is {score}')

    return score



filename = "adventofcode/10-syntax-scoring.txt"

#puzzle1(filename)

puzzle2(filename)
