#https://adventofcode.com/2021/day/14


def load1(file='adventofcode/temp.txt'):

    with open(file, 'r') as f:
        template,rules = f.read().split('\n\n')
        #print(template,rules)
    
    rplMap = {}
    for rr in rules.split("\n"):
        elem, insrt = rr.split(" -> ")
        #print(f"{elem=},{insrt=}")
        #rplMap[elem] = (elem[0] + insrt, insrt + elem[1])
        rplMap[elem] = elem[0] + insrt
    
    #print(rplMap)

    return template, rplMap

def load2(file='adventofcode/temp.txt'):

    with open(file, 'r') as f:
        template,rules = f.read().split('\n\n')
        #print(template,rules)
    
    rplMap = {}
    for rr in rules.split("\n"):
        elem, insrt = rr.split(" -> ")
        #print(f"{elem=},{insrt=}")
        rplMap[elem] = (elem[0] + insrt, insrt + elem[1])
        #rplMap[elem] = elem[0] + insrt
    
    #print(rplMap)

    return template, rplMap

# This will not scale for large strings. Puzzle2 times out with this style.
def pairInsertStep(template, rplMap):

    newTemplate = ''

    for ii in range(len(template)):
        ky = template[ii:ii+2] 
        #print(f'{ky=}')
        if ky in rplMap:
            newTemplate = newTemplate + rplMap[ky]
        elif len(ky) == 1:
            newTemplate = newTemplate + ky

    return newTemplate

def puzzle1():
    
    template, rplMap =  load1(file='adventofcode/14-extended-polymerization.txt')

    for ii in range(10):
        #print(f'Doing Step {ii=}')
        template = pairInsertStep(template, rplMap)
        #print(template)
    
    #print(template)

    counters = {}

    for cc in template:
        if cc in counters:
            counters[cc] = counters[cc] + 1
        else:
            counters[cc] = 1

    #print(counters)

    maxK = None
    minK = None
    
    maxV = 0
    minV = 0
    for k in counters:
        v = counters[k]
        if maxK is None or v > maxV:
            maxV = v
            maxK = k
        
        if minK is None or v < minV:
            minV = v
            minK = k

    print(f"Puzzle 1: Expected 2947. Calculated {counters[maxK] - counters[minK]}")



def doStep(old_pair_counts, rplMap):

    new_pair_counts = {}

    for key in old_pair_counts:
        if key in rplMap:         
            # This key is being replaced.
            times2Insert = old_pair_counts[key]

            # 2 new keys are being added.
            for key2insrt in rplMap[key]:

                if key2insrt in new_pair_counts:
                    new_pair_counts[key2insrt] += times2Insert
                else:
                    new_pair_counts[key2insrt] = times2Insert
                
        else:
            #do nothing. 
            pass

    return new_pair_counts

def createCharCounts(pair_counts):
    cc = {}

    for pc in pair_counts:
        for chars in pc:
            if chars not in cc:
                cc[chars] = pair_counts[pc]
            else:
                cc[chars] += pair_counts[pc]

    return cc


def puzzle2():

    template, rplMap =  load2(file='adventofcode/14-extended-polymerization.txt')
    #template, rplMap =  load2()
    # NNCB 
    # {'CH': ('CB', 'BH'), 'HH': ('HN', 'NH')}

    # Instead of building new strings (or polymer), lets just keep a count of the pairs instead.

    pair_counts = {}
    for ii in range(len(template)):
        key = template[ii: ii+2]
        if len(key) > 1:
            if key in pair_counts:
                pair_counts[key] += 1
            else:
                pair_counts[key] = 1

    #print(template, pair_counts) # NNCB {'NN': 1, 'NC': 1, 'CB': 1}
    #print(rplMap) #{'CH': ('CB', 'BH'), 'HH': ('HN', 'NH')}

    #print(pair_counts)
    for ii in range(40):
        #print(f"Doing Step {ii=}")
        pair_counts = doStep(pair_counts, rplMap)
        #print(pair_counts)

    #print(pair_counts) #{'NB': 796, 'BB': 812, 'BN': 735, 'BC': 120}

    #print( sum(pair_counts[key] for key in pair_counts) )

    rawCharCounts = createCharCounts(pair_counts)
    #print(rawCharCounts) #{'N': 1729, 'B': 3497, 'C': 596, 'H': 322}

    # First and last char will never change and will remain at the first and last place repectively after all steps are done.
    fc = template[0]
    lc = template[-1]

    # The chars are double counted except the first and last one. So need to create a calibrated count dict.
    calibratedCounts = {}
    for key in rawCharCounts:
        newCount = rawCharCounts[key] // 2
        if key == fc or key == lc:
            newCount += 1
        calibratedCounts[key] = newCount
    
    #print(calibratedCounts) #{'N': 865, 'B': 1749, 'C': 298, 'H': 161}

    answer = max(calibratedCounts[key] for key in calibratedCounts) - min(calibratedCounts[key] for key in calibratedCounts) 
    
    print(f"Puzzle 2: Expected 3232426226464. Calculated {answer=}")

puzzle1()
puzzle2()


