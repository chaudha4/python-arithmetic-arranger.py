# https://adventofcode.com/2021/day/12

def load(file="adventofcode/temp.txt"):

    data = {}
    with open(file, "r") as f:
        row = f.read().split()
        # ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']
                
        for rr in row:
            # 'start-A'
            key, value = rr.split("-")
            if key in data:
                data[key].append(value)
            else:
                data[key] = [value]
            
            # Do the reverse as well except for Start and end
            if (key == 'start' or value == 'end'):
                pass
            else:
                if value in data:
                    data[value].append(key)
                else:
                    data[value] = [key]                

    # {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'b': ['d', 'end']}
    # {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'c': ['A'], 'b': ['A', 'd', 'end'], 'd': ['b']}
    #print(data)
            
    return data


pathcount = 0

def bfs(graph, frm = "start", to = "end", visited = set(), path = []):
    
    global pathcount
    #print(f'Processing from {frm} to {to} for graph {graph} visted {visited}')
    
    if frm.islower():
        visited.add(frm)

    for node in graph[frm]:
        path.append(frm)
        if node == to:
            print(f'Reached end from {frm} visitng {visited} taking path {path}')
            pathcount += 1
        elif node not in visited:
            #if node.islower():
             #   visited.add(node)
            bfs(graph, node, to, visited, path)
        path.pop()

    if frm in visited:
        visited.remove(frm)
            
    


def puzzle1():

    data = load("adventofcode/12-passage-pathing.txt")
    #data = load()
    #print(paths(data))
    bfs(data)
    print(f'Total Paths is {pathcount}')
    #bfs(data, "b")

puzzle1()
