
# https://adventofcode.com/2021/day/8

"""


Facts:
1 is the only digit that uses two segments
7 is the only digit that uses three segments
4 is the only digit that uses four segments
2,3,5 uses 5 segments
6,9 used 6 segments
8 is the only digit that uses all segments(7)

"""
def decode(data):

    print("")
    segs = data.split()
    lkup = {}

    two35, six9 = [], []
    one, four, seven, eight = "", "", "", ""

    # Group segments
    for sg in segs:
        sz = len(sg)
        if sz == 2:
            one = "".join(sorted(sg))
            lkup[one] = 1
        elif sz == 3:
            seven = "".join(sorted(sg))
            lkup[seven] = 7
        elif sz == 4:
            four = "".join(sorted(sg))
            lkup[four] = 4
        elif sz == 5:
            two35.append(sg)
        elif sz == 6:
            six9.append(sg)
        elif sz == 7:
            eight = "".join(sorted(sg))
            lkup[eight] = 8
    

    # Find 9 - 4 is contained in 9 (but not in 0,6)
    nine = ""
    for seg in six9:
        is9 = True
        for c in four:
            if seg.find(c) == -1:
                is9 = False
                break
        if (is9):
            nine = "".join(sorted(seg))
            lkup[nine] = 9
            break


    # Find 0 - 7 is contained in 0 and 9. But since we know 9, we can find 0.
    zero = ""
    for seg in six9:
        temp = "".join(sorted(seg))
        if ( temp != nine ):
            is0 = True
            for c in seven:
                if temp.find(c) == -1:
                    is0 = False
                    break
            if (is0):
                zero = temp
                lkup[zero] = 0
                break


    # Find 6: The leftover must be 6
    six = ""
    for seg in six9:
        temp = "".join(sorted(seg))
        if ( temp != nine and temp != zero):
            six = temp
            lkup[six] = 6
            break
    

    # Find 5 : 5 is contained in 6 (2 and 3 are not)
    five = ""
    for seg in two35:
        is5 = True
        for c in seg:
            if six.find(c) == -1:
                is5 = False
                break
        if (is5):
            five = "".join(sorted(seg))
            lkup[five] = 5
            break        

    # Find 3 : 3 is contained in 9 (2 is not and discard 5 since we know it)
    three = ""
    for seg in two35:
        is3 = True
        temp = "".join(sorted(seg))
        if temp != five:
            for c in temp:
                if nine.find(c) == -1:
                    is3 = False
                    break
            if (is3):
                three = temp
                lkup[three] = 3
                break        

    # Find 2: The leftover must be 6
    two = ""
    for seg in two35:
        temp = "".join(sorted(seg))
        if ( temp != three and temp != five):
            two = temp
            lkup[two] = 2
            break

    print("----Decoded Data----")
    print(lkup)
    return lkup



def getNum(mydict, data):
    num = ""
    for sg in data.split():
        #print(sg)
        temp = "".join(sorted(sg))
        num = num + str(mydict[temp])
    
    print("Number decoded is: ", int(num))
    return int(num)

def load_data(file="adventofcode/temp.txt"):

    total = 0
    with open(file, "r") as f:
        sz = 0
        row = f.read().split("\n")
        for rr in row:
            data = rr.split("|")
            #print(data[0], data[1])
            #sz = sz + count1478(data[1])
            mydict = decode(data[0])
            number = getNum(mydict, data[1])
            total = total + number
    
    print("-" * 60)
    print("Sum of all numbers decoded: ", total)
    print("-" * 60)

# puzzle 1
def count1478(data):
    cnt = 0
    for dd in data.split():
        sz = len(dd)
        if (sz == 2 or sz == 3 or sz == 4 or sz == 7):
            cnt = cnt + 1

    return cnt




load_data("/home/chaudha4/Projects/Python-Projects/adventofcode/08-seven-segment-search.txt")
#load_data()
