

def isCorruptedLine(row):

    line = list(row)

    valid_close = [")", "]", "}", ">"]
    
    valid = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    
    
    index = 0
    #print(line)
    for ii, cc in enumerate(line):

        #print("Processing, ", ii, cc)
        if cc == '':
            continue
        elif cc in valid:
            index = ii
            #print("Valid Close detected at, ", ii, cc)
        
            #go reverse and look for match
            fnd = False
            for jj in range(ii-1,-1,-1):
                if line[jj] == '':
                    continue
                elif line[jj] == valid[cc]:
                    line[ii] = ''
                    line[jj] = ''
                    fnd = True
                    #print(line)
                    break
                else:
                    print("This is a corrupted line - detected mismatch at index ", index, line[jj], cc)
                    return True
    return False



with open("adventofcode/temp.txt", "r") as f:
    data = f.read().split("\n")
    for row in data:
        rst = isCorruptedLine(row)
        print(rst, row)



