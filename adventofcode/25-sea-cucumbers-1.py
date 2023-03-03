# https://adventofcode.com/2021/day/25

from collections import defaultdict

def load(file:str ='adventofcode/25-data.txt') -> list:

    rows = []
    with open(file) as f:
        rows = f.read().strip().split('\n')
       
    data = list(list(val for val in row) for row in rows)
    # data = [[val for val in row] for row in rows]
    
    return data

def load_test(file:str ='adventofcode/25-sea-cucumbers.txt') -> list:

    data = defaultdict(list)

    rows = []
    with open(file) as f:
        rows = f.read().strip().split('\n\n')

    for row in rows:
        aa, bb = row.split(':\n')
        key = aa.split(' ')[1] # Extract 1 out of "After 1 step:"
        moves = bb.split("\n")
        val = list(list(val for val in rr) for rr in moves)
        data[key] = val
    
    return(data)
    
    
    
# This funtion will update the data passed in and will return a flag indicating if no updates were done.

def take_step(data):

    updated = False

    # First process east steps
    rc = len(data)
    cc = len(data[0])

    # First process east steps
    for ii in range(rc):
        can_move = set() # Track cells that can move
        for jj in range(cc):
            element = data[ii][jj]
            # Move horizontally
            if element == ">":
                target_loc = jj + 1
                if target_loc >= cc:
                    target_loc = 0
                if data[ii][target_loc] == '.':
                    can_move.add((jj,target_loc))
        # Now move horizontally
        for frm, to in can_move:
            updated = True
            data[ii][frm] = '.'
            data[ii][to] = '>'

    # Now process south steps
    for jj in range(cc):
        can_move = set() # Track cells that can move
        for ii in range(rc):       
            element = data[ii][jj]
            if element == "v":
                target_loc = ii + 1
                if target_loc >= rc:
                    target_loc = 0

                if data[target_loc][jj] == '.':         
                    can_move.add((ii,target_loc))                
        # Now move Vertically
        for frm, to in can_move:
            updated = True
            data[frm][jj] = '.'
            data[to][jj] = 'v'

    return updated

def pdata(data, newdata=None):
    print()
    if newdata:
        for r1, r2 in zip(data, newdata):
            print(r1)
            print(r2)
            print()
    else:
        for r in data:
            print(r)

def test1():
    test_data = load_test()
    data = test_data['0']

    ii = 1
    while take_step(data):
        print(f'Testing step {ii}')

        # Compare the results
        expected = test_data[str(ii)]
        errors = []
        for xx in range(len(expected)):
            for yy in range(len(expected[xx])):
                if expected[xx][yy] != data[xx][yy]:
                    errors.append(((xx,yy), f'expected {expected[xx][yy]}', f'Actual {data[xx][yy]}'))
        
        if len(errors) > 0:
            print(errors)
            pdata(data, expected)
            assert False
        
        print(f'Step {ii} passed.\n')
        ii += 1
        
    print(f'Stopped at step {ii}')
                    

def sol1():
    data = load()

    ii = 1
    while take_step(data):
        ii += 1
        
    print(f'Stopped at step {ii}. Expected 384.')
    assert ii == 384
                    

sol1()
#test1()
