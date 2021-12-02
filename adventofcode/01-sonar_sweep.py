"""
https://adventofcode.com/2021/day/1
"""

def part1():
    with open("/localdisk/github/Python-Projects/adventofcode/sonar_sweep.txt", "r") as f:
        #data = f.read()
        data = f.read().split()
        print(len(data))
        
        count = 0

        prev = None
        
        for d in data:
            curr = int(d)
            if prev is None:
                prev = curr
                continue
            
            if (curr >  prev):
                count = count + 1


            prev = curr

        print(count)


def part2():

    data = []
    with open("/localdisk/github/Python-Projects/adventofcode/sonar_sweep.txt", "r") as f:
        data = [ int(d) for d in f.read().split() ]

    print(data)
    count = 0
    for ii in range(len(data)-3):
        if (data[ii+1] + data[ii+2] + data[ii+3]) > (data[ii+1] + data[ii+2] + data[ii]):
            count = count+1

    print(count)

part2()