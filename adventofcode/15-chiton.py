#https://adventofcode.com/2021/day/15

#https://github.com/womogenes/AoC-2021-Solutions/blob/main/day_15/day_15_p1.py


import heapq
from collections import defaultdict

def load(file='adventofcode/temp.txt'):

    risk = []
    with open(file, 'r') as f:
        lines = f.read().split("\n")
        # print(lines) # ['1163751742', '1381373672',]

        for line in lines:
            cols = [int(cc) for cc in line ]
            risk.append(cols)   
    return risk

# This will be slow as it is a brute force solution. It tries to find all possible paths and their costs. WIll not scale.

def dfs_solution(risk, x, y):

    visited = set()
    #visited.add(( ((x,y),), risk[x][y],))
    visited.add(( ((x,y),), 0,))

    completed_paths = set()
    min_risk_so_far = None

    numr = len(risk)
    numc = len(risk[0])

    while len(visited):


        visited_paths_risks =  visited.pop()
        # print(visited_paths_risks)
        visited_paths, visited_risks = visited_paths_risks
        # print(visited_paths)
        xy = visited_paths[-1] # coordinate to be processed next
        # print(f'Processing {xy=} with {visited_risks=} {visited_paths=}')


        next = [
            #(xy[0]-1, xy[1]),
            (xy[0]+1, xy[1]),
            #(xy[0], xy[1]-1),
            (xy[0], xy[1]+1),
        ]

        for nn in next:
            X = nn[0]
            Y = nn[1]
            if 0 <= X < numc and 0 <= Y < numr and (X, Y) not in visited_paths:
                if X == numc - 1 and Y == numc - 1: 
                    # reached end point. No need to process this path any further.
                    print(f'Reached Destination - Path taken {visited_paths} with risk {visited_risks}')                   
                    completed_paths.add( ( (*visited_paths,(X, Y)), visited_risks + risk[X][Y]) )
                    if min_risk_so_far is None or min_risk_so_far > visited_risks:
                        min_risk_so_far = visited_risks
                else:
                    if min_risk_so_far is None or visited_risks < min_risk_so_far:
                        visited.add( ( (*visited_paths,(X, Y)), visited_risks + risk[X][Y]) )

        #break

        # print(visited)

    return completed_paths


def dijkstra_solution(costs, x, y):

 
    newcosts = defaultdict(int)
    visited = set()         # keep a list of cells visited. No need to track the path taken.
    todo = []
    stopAt = len(costs)

    heapq.heapify(todo) # Pop the lowest cost for each node. Discard rest since they will bemore expensive.
    heapq.heappush(todo, (0, x, y))  # the cost to go to start(self) is always zero.

    while len(todo):

        cost, x, y = heapq.heappop(todo)

        if (x,y) in visited:
            continue

        visited.add((x, y))
        newcosts[(x, y)] = cost


        if x == stopAt - 1 and y == stopAt - 1: # Reached Destination Cell.
            break

        next = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
        ]

        #print(f'Now processing {cost=} {cell=}')
        for xx, yy in next:
            if 0 <= xx < stopAt and 0 <= yy < stopAt:
                heapq.heappush(todo, (cost + costs[xx][yy], xx, yy))
                    
      
    return newcosts


         
            
def puzzle1():
    costs = load("adventofcode/15-chiton.txt")
    #costs = load()
    stopAt = len(costs)
    cumulative_costs = dijkstra_solution(costs,0,0)
    #print(cumulative_costs)
    minCost=cumulative_costs[(stopAt-1,stopAt-1)]
    print(f'Puzzle1: Expected 619. Calculated {minCost=}')


def getCost(costs, x, y):
    maxVal = len(costs)
    xx = x % maxVal # this will keep the xx in costs range
    yy = y % maxVal

    cost = costs[xx][yy] + (x//maxVal) + (y//maxVal)
    if cost > 9:
        cost = cost - 9
    return cost

def testGetCost():
    costs = load()
    #print(costs)
    for ii in range(50):
        print(getCost(costs,ii,0), end=",")

    print()
    for ii in range(50):
        print(getCost(costs,ii,10), end=",")

    print()
    for ii in range(50):
        print(getCost(costs,0,ii), end=",")

    print()
    for ii in range(50):
        print(getCost(costs,49,ii), end=",")

    print()
    for ii in range(50):
        print(getCost(costs,ii,49), end=",")

    print()



def dijkstra_puzzle2_solution(costs):

    stopAt = len(costs) * 5
    visited = set()
    todo = [(0,0,0)] # Cost, X, Y
    heapq.heapify(todo)

    while len(todo):
        
        cost, x, y = heapq.heappop(todo)

        if (x,y) in visited:
            continue

        visited.add((x,y))

        if x == stopAt - 1 and y == stopAt - 1: # Reached Destination Cell.
            return cost

        next = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
        ]

        #print(f'Now processing {cost=} {cell=}')
        for xx, yy in next:
            if 0 <= xx < stopAt and 0 <= yy < stopAt:
                toAddCost = getCost(costs, xx, yy)
                heapq.heappush(todo, (cost + toAddCost, xx, yy))

def puzzle2():
    costs = load("adventofcode/15-chiton.txt")
    minCost = dijkstra_puzzle2_solution(costs)
    print(f'Puzzle1: Expected 2922. Calculate {minCost=}')


def puzzle3():
    costs = load("adventofcode/15-chiton.txt")
    minCost = dijkstra_solution_track_min_cost_path(costs)
    print(f'Puzzle1: Expected 2922. Calculate {minCost=}')




def dijkstra_solution_track_min_cost_path(costs):

    stopAt = len(costs)
    visited = set()
    todo = [(0,[(0,0)])] # Cost, X, Y
    heapq.heapify(todo)

    while len(todo):
        
        cost, pathsofar = heapq.heappop(todo)
        
        x, y  = pathsofar[-1]
        
        if (x,y) in visited:
            continue

        visited.add((x,y))

        #print(f'Processing {x=} {y=} {cost=}')
        if x == stopAt - 1 and y == stopAt - 1: # Reached Destination Cell.
            print(pathsofar)
            return cost

        next = [
            (x-1, y),
            (x+1, y),
            (x, y-1),
            (x, y+1),
        ]

        #print(f'Now processing {cost=} {cell=}')
        for xx, yy in next:
            if 0 <= xx < stopAt and 0 <= yy < stopAt:
                newCost = cost + getCost(costs, xx, yy)
                newPaths = [*pathsofar, (xx,yy)]
                heapq.heappush(todo, (newCost, newPaths))

#testGetCost()  
#puzzle1()
#puzzle2()
puzzle3()





