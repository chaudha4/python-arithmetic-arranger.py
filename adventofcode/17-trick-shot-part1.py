#https://adventofcode.com/2021/day/17

import logging

#logging.basicConfig(level=logging.INFO)


def fire_probe(x, y, xv, yv, target_x, target_y, highest_y_seen=0):

    logging.debug(f'{x=} {y=} {xv=} {yv=} {target_x=} {target_y=}')

    next_x = x + xv
    next_y = y + yv

    if next_y > highest_y_seen:
        highest_y_seen = next_y

    # x velocity changes by 1 toward the value 0
    if xv < 0:
        xv = xv+1
    elif xv > 0:
        xv = xv-1

    # y velocity decreases by 1. It can be negative since it is relative to the speed thrown.
    yv = yv - 1

    # Did we land. Return True if we did
    if target_x[0] <= next_x <= target_x[1] and target_y[0] <= next_y <= target_y[1]:
        logging.info(f'Landed with {x=} {y=} {xv=} {yv=} {next_x=} {target_x=} {next_y=} {target_y=} {highest_y_seen=}')
        return True, highest_y_seen

    # Did we overshoot. Return False to indicate we overshot the Target area
    if next_x > target_x[1] or next_y < target_y[0]:
        logging.debug(f'Overshot with {next_x} > {target_x[1]} or {next_y}  < {target_y[0]}. {target_x=} {target_y=}')
        return False, highest_y_seen

    # We have more to travel
    return fire_probe(next_x, next_y, xv, yv, target_x, target_y, highest_y_seen)


def test1():
    logging.basicConfig(level=logging.DEBUG)

    result, highest_seen = fire_probe(0,0,6,0,(20,30,),(-10,-5,))
    print(f'{result=} {highest_seen=}\n')

    result, highest_seen = fire_probe(0,0,7,2,(20,30,),(-10,-5,))
    print(f'{result=} {highest_seen=}\n')

    result, highest_seen = fire_probe(0,0,6,3,(20,30,),(-10,-5,))
    print(f'{result=} {highest_seen=}\n')

    result, highest_seen = fire_probe(0,0,17,-4,(20,30,),(-10,-5,))
    print(f'{result=} {highest_seen=}\n')

    result, highest_seen = fire_probe(0,0,9,0,(20,30,),(-10,-5,))
    print(f'{result=} {highest_seen=}\n')

# Solution is brute force. I cannot think of a better way to handle this !!
def solution1():

    rxx = 0
    ryy = 0
    highest_seen = 0

    for xx in range(-100,100,1):
        for yy in range(0,263,1):           
            result, hs = fire_probe(0,0,xx,yy,(85,145,),(-163,-108,))
            if result:
                if hs > highest_seen:
                    highest_seen = hs
                    rxx = xx
                    ryy = yy
                #print(f'{xx=} {yy=} {highest_seen=}')

    print(f'{rxx=} {ryy=} {highest_seen=} Expected=13203')            

if __name__ == '__main__':
    #test1()
    solution1()
    




    
