# https://adventofcode.com/2021/day/12

import collections as cs

def load(file="adventofcode/temp.txt"):

    # Here we create a Graph data structure that will hold the adjacency list. The key is node and value is a list of reachable nodes.
    # The graph is unidirectional from start (and to end). It is bidirectional for all other nodes. So we need special handling for that.
    # data = {} # Python dict will throw exception if key not found
    data = cs.defaultdict(list) # the values will be a list.
    with open(file, "r") as f:
        row = f.read().split()
        # ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']
                
        for rr in row:
            key, value = rr.split("-")
            data[key].append(value)
            data[value].append(key)

            # Need this for python dictionary but not for collections.defaultdict
            
            # if key in data:
            #     data[key].append(value)
            # else:
            #     data[key] = [value]
            
            # # Do the reverse as well except for Start and end
            # if (key == 'start' or value == 'end'):
            #     pass
            # else:
            #     if value in data:
            #         data[value].append(key)
            #     else:
            #         data[value] = [key]                

    # {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'b': ['d', 'end']}  <--- We don't want this.
    # {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'd': ['b']}   <--- We want this !!
    #print(data)
            
    return data


pathcount = 0

# We are using Depth First Search using recursion. Another way would be to use a stack. DFS is faster
# than BFS and in BFS, there is no concept of backtracking. We don't need backtracking for this excercise
# but for debugging, it is better to see the path we took.

def puzzle1_dfs_using_regression(graph, frm = "start", to = "end", path = []):
    
    global pathcount
    #print(f'Processing from {frm} to {to} for graph {graph} visted {visited}')
   

    for node in graph[frm]:
        path.append(frm) # Track the path. Every regression path will get its own uniqiue list
        if node == to:
            # If we are here, regression ended.
            pathcount += 1
        elif node not in path or node.isupper(): 
            puzzle1_dfs_using_regression(graph, node, to, path)
        
        #This will go to the next branch in the graph.
        path.pop() #backtracking - typical in regression !! 


def dfs_using_list(graph, frm = "start", to = "end"):

    toProcessPaths = [[frm]] # [[start,a], [start,b,s]]
    allPaths = [] #For debugging
    count = 0

    while toProcessPaths:
        
        currPath = toProcessPaths.pop()
        #print(currPath)

        if currPath[-1] == to: # Reached end for current path. Skip this loop.
            count += 1
            allPaths.append([*currPath])
            continue

        for nn in graph[currPath[-1]]:
            if nn not in currPath or nn.isupper():
                toProcessPaths.append([*currPath, nn])


    #print(allPaths)
    print(count)
    return count

 # How many paths through this cave system are there that visit small caves at most once?
def puzzle1():

    data = load("adventofcode/12-passage-pathing.txt")
    #data = load()
    #print(paths(data))
    puzzle1_dfs_using_regression(data)
    dfs_using_list(data)
    print(f'Total Paths is {pathcount}. Expected 3495.')
    #bfs(data, "b")


# We are using Depth First Search using recursion. Another way would be to use a stack. DFS is faster
# than BFS and in BFS, there is no concept of backtracking. We don't need backtracking for this excercise
# but for debugging, it is better to see the path we took.

puzzle2_cnt = 0

def puzzle2_dfs_using_regression(graph, frm = "start", to = "end", path = [], doneTwice = False):
    
    #print(f'Processing from {frm} to {to} for graph {graph} visted {visited}')
   
    global puzzle2_cnt

    for node in graph[frm]:
        path.append(frm) # Track the path. Every regression path will get its own uniqiue list
        if node == to:
            # If we are here, regression ended.
            puzzle2_cnt += 1
        elif node not in path or node.isupper(): 
            puzzle2_dfs_using_regression(graph, node, to, path, doneTwice)
        elif not doneTwice and node.islower() and node != 'start':
            puzzle2_dfs_using_regression(graph, node, to, path, True)


        
        #This will go to the next branch in the graph.
        path.pop() #backtracking - typical in regression !! 

    return puzzle2_cnt


def puzzle2():

    data = load("adventofcode/12-passage-pathing.txt")
    #data = load()
    #print(paths(data))
    puzzle2_dfs_using_regression(data)
    print(f'Found {puzzle2_cnt} paths. Expected should be 94849')
    #bfs(data, "b")




puzzle2()
