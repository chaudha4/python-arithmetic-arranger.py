import logging
import math

#https://adventofcode.com/2021/day/18


def explode(inputList):
    
    assert type(inputList) == list

    count = 0
    idx1 = None
    idx1Set = False
    idx2 = None
    idx2Set = False
    n1 = None
    n1Idx = None
    n2 = None
    n2Idx = None

      
    # Find the leftmost pair nested inside four outer pairs. Save the index in idx1:idx2
    for i, c in enumerate(inputList):
        if c == "[":
            count = count + 1
            if not idx1Set and count == 5:
                idx1Set = True
                idx1 = i
        elif c == "]":
            count = count - 1
            if idx1Set:
                if not idx2Set:
                    idx2 = i
                    idx2Set = True          
        elif c.isnumeric():
            if idx1Set == False:
                n1 = c
                n1Idx = i
            else:
                if idx2Set == True and n2 is None:
                    n2 = c 
                    n2Idx = i

    #print(f'{idx1=} {idx2=} {inputStr[idx1:idx2]} {n1=} {n2=} {n1Idx=} {n2Idx=}')

    # NOTHING TO EXPLODE.
    if idx1 is None:
        #Try Split Next
        # if split produces a pair that meets the explode criteria, that pair explodes before other splits occur.
        return split(inputList)
    
    

    assert count == 0, f"Mismatched Pairs {count=} {inputList=}"

    # Extract the pair to be exploded and save it in arr
    arr = []
    for c in inputList[idx1:idx2]:
        if c.isnumeric():
            arr.append(int(c))
    

    assert len(arr) == 2, f"Every Pair must have 2 entries {arr=} {count=} {inputList=}"


    #find the first regular number to the left of the exploding pair
    if n1Idx is not None:
        old = int(n1)
        n1 = old + arr[0]
        inputList[n1Idx] = str(n1)


    ##find the first regular number to the right of the exploding pair
    if n2Idx is not None:
        old = int(n2)
        n2 = old + arr[1]
        inputList[n2Idx] = str(n2)

    explodedList = []

    # Replace [x,y] with a 0
    insertZero = False
    for i, c in enumerate(inputList):
        if i < idx1 or i > idx2:
            explodedList.append(c)
        else:
            # exploding pair is replaced with the regular number 0
            if not insertZero:
                insertZero = True
                explodedList.append("0")

    #print(f'{explodedList=}')

    return explodedList, True

def split(inputList):

    assert type(inputList) == list

    didSplit = False
    splitList = []

    for i, c in enumerate(inputList):
        if not didSplit and c.isnumeric() and int(c) > 9:
            # Need to Split
            nn = int(c) / 2
            didSplit = True
            splitList.append("[")           
            splitList.append(f'{math.floor(nn)}')
            splitList.append(",")
            splitList.append(f'{math.ceil(nn)}')
            splitList.append("]")
        else:
            splitList.append(c)

    # If we did a split, that could result in a need to explaode again. The didSplit will be tru and that will trigger one more 
    # explode in the explode().
    return splitList, didSplit


def add(left, right):
    assert type(left) == str
    assert type(right) == str

    addedList = f'[{left},{right}]'
    expList = convert2list(addedList)
    explodeMore = True

    # Explode till we don't need to. Explode will also do a split.
    while explodeMore:
        expList, explodeMore = explode(expList)

    return convert2String(expList)

def getMagnitude(inputList):

    assert type(inputList) == list

    if len(inputList) == 1:
        return inputList    
    
    newList = []

    Prev = None
    xIndex = None
    yIndex = None

    for i, c in enumerate(inputList):
        newList.append(c)
        if c.isnumeric():
            if prev == '[':
                # multiply by 3
                xIndex = i
            elif prev == ',':
                if xIndex is not None:
                    yIndex = i
        elif c == "]":
            if yIndex is not None:
                # we found a [X,Y] pattern
                x = int(inputList[xIndex])
                y = int(inputList[yIndex])
                z = (3*x) + (2*y)
                #replace the last entry with this new entry
                newList = newList[:-5]
                newList.append(str(z))

                #Reset the flags
                xIndex = None
                yIndex = None

        prev = c
    
    #print(newList)

    
    return getMagnitude(newList)

def testGetMagnitude():
    test = [ 
        ('[9,1]', 29),
        ('[[9,1],[1,9]]', 129),
        ('[[1,2],[[3,4],5]]', 143),
        ('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', 1384),
        ('[[[[1,1],[2,2]],[3,3]],[4,4]]', 445),
        ('[[[[3,0],[5,3]],[4,4]],[5,5]]', 791),
        ('[[[[5,0],[7,4]],[5,5]],[6,6]]', 1137),
        ('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]', 3488),
    ]

    for val in test:
        pair = convert2list(val[0])
        result = getMagnitude(pair)
        mm = int(result[0])
        assert mm ==  val[1], f'Test Failed. {val=} {result=}'
        print(f'Test passed for {val}')

def solution2():
    with open("./adventofcode/18-snailfish.txt") as f:
        largestMagnitude = 0
        lines = f.read().split()
        prevPair = None
        for currPair in lines:
            if prevPair is not None:
                result = add(prevPair, currPair)
                mlist = getMagnitude(convert2list(result))
                mval = int(mlist[0])
                if mval > largestMagnitude:
                    largestMagnitude = mval

                #Note that addition is not commutative - that is, x + y and y + x can produce different results. So try other way too
                result = add(currPair, prevPair)
                mlist = getMagnitude(convert2list(result))
                mval = int(mlist[0])
                if mval > largestMagnitude:
                    largestMagnitude = mval
                                
            prevPair = currPair
 
        print(f'The largest magnitude seen is {largestMagnitude=}')

# Need this function to handle numbers greater than 9. For Example 24 should not be parsed as "2" and "4"
def convert2list(inputStr):
    assert type(inputStr) == str

    arr = []
    num = ""
    numStart = False

    for c in inputStr:
        
        if c.isnumeric():
            if numStart:
                # Number accumulation in progress. Continue accumulating.
                num = num + c
            else:
                # Number accumulation started.
                numStart = True
                num = c
        else:
            if numStart:
                # Number accumulation in progress. Stop accumulating and save it.
                arr.append(num)
                numStart = False
                num = ""
            arr.append(c)
    
    #print(arr)
    return arr

def convert2String(inputList):
    assert type(inputList) == list

    retStr = ""

    for c in inputList:
        retStr = retStr + c

    return retStr

def testConvert2list():
    test = [
        '[[[[[94,8],14],2],43],45]',
        '[7,[6,[5,[4,[3,2]]]]]',
        '[[6,[5,[4,[3,2]]]],1]',
        '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]',
        '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]',
        '[[[[01,70],34],[72,[[10,43],93]]],[11,12]]',
        '[[[[0,9],2],3],4]',
    ]

    for t in test:
        result = convert2list(t)
        print(result)

def testExplode():
    test = [
        '[[[[[9,8],1],2],3],4]',
        '[7,[16,[5,[4,[3,2]]]]]',
        '[[6,[5,[4,[3,2]]]],1]',
        '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]',
        '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]',
        '[[[[0,7],4],[7,[[8,4],9]]],[1,1]]',
        '[[[[0,9],2],3],4]',
    ]

    expected = [
        '[[[[0,9],2],3],4]',
        '[7,[16,[5,[7,0]]]]',
        '[[6,[5,[7,0]]],3]',
        '[[3,[2,[8,0]]],[9,[5,[7,0]]]]',
        '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]',
        '[[[[0,7],4],[15,[0,13]]],[1,1]]',
        '[[[[0,9],2],3],4]'
    ]    

    for t, r in zip(test, expected):
        print(f'Now Testing {t=}')
        arr = convert2list(t)
        expList, didItExplode = explode(arr)
        expStrng = convert2String(expList)
        assert expStrng == r, f'Got {expStrng=} - Expected {r=}'
        print(f'Success Got:{expStrng} - Expected:{r} - Did it Explode:{didItExplode}')
        #assert splitNeeded == r[1]

def testMultipleExplode():

    expList = convert2list('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
    doMore = True
    while doMore:
        expList, doMore = explode(expList)
        print(convert2String(expList))

def testSplit():
    splitList = convert2list('[[[[0,7],4],[15,[0,13]]],[1,1]]')
    doMore = True
    while doMore:
        splitList, doMore = split(splitList)
        print(f'After Split:{convert2String(splitList)}, Split was done:{doMore}')

def test_add():

    result = add('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]')
    assert result == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', f'{result=}'

# testExplode()
# testMultipleExplode()
# test_add()
# testConvert2list()
# testSplit()
# solution2()
# testGetMagnitude()