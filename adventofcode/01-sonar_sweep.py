"""
https://adventofcode.com/2021/day/1
"""

def puzzle1():
    with open("adventofcode/01-sonar_sweep.txt", "r") as f:
        #data = f.read()
        data = f.read().split()
        #print(len(data))
        
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

        print(f'1. Found measurements {count=} than the previous measurement. Expected 1482')

        count = 0
        for kk in range(1, len(data)):
            if int(data[kk]) > int(data[kk-1]):
                count += 1

        print(f'2. Found measurements {count} than the previous measurement. Expected 1482')


def puzzle2():

    testdata = [199,200,208,210,200,207,240,269,260,263]
    data = []
    with open("adventofcode/01-sonar_sweep.txt", "r") as f:
        data = [ int(d) for d in f.read().split() ]

    #print(data)
    count = 0
    for ii in range(len(data)-3):
        if (data[ii+1] + data[ii+2] + data[ii+3]) > (data[ii+1] + data[ii+2] + data[ii]):
            count = count+1

    print(f'5. Three-measurement sliding window count is {count}. Expected 1518.')

    # A more efficient way would be to only look at the first and fourth. If 4th is more than Ist, the sliding 
    # window sum must be increasing since 2nd and 3rd are common in both windows.
    # Found this here - https://youtu.be/zcunDS2RoRk

    count = 0
    for ii in range(len(data)-3):
        #print(ii,data[ii],data[ii+3])
        if (data[ii] < data[ii+3]):
            count += 1
    print(f'6. Three-measurement sliding window count is {count}. Expected 1518.')


    # Another variation !!
    count = 0
    for kk in range(3, len(data)):
        if int(data[kk]) > int(data[kk-3]):
            count += 1

    print(f'7. Found measurements {count} than the previous measurement. Expected 1518')



puzzle1()
puzzle2()