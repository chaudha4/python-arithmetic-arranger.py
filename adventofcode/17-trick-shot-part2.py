#https://adventofcode.com/2021/day/17#part2

import logging

#logging.basicConfig(level=logging.INFO)


def fire_probe(x, y, xv, yv, target_x, target_y,):

    logging.debug(f'{x=} {y=} {xv=} {yv=} {target_x=} {target_y=}')

    next_x = x + xv
    next_y = y + yv


    # x velocity changes by 1 toward the value 0
    if xv < 0:
        xv = xv+1
    elif xv > 0:
        xv = xv-1

    # y velocity decreases by 1. It can be negative since it is relative to the speed thrown.
    yv = yv - 1

    # Did we land. Return True if we did
    if target_x[0] <= next_x <= target_x[1] and target_y[0] <= next_y <= target_y[1]:
        logging.info(f'Landed with {x=} {y=} {xv=} {yv=} {next_x=} {target_x=} {next_y=} {target_y=}')
        return True

    # Did we overshoot. Return False to indicate we overshot the Target area
    if next_x > target_x[1] or next_y < target_y[0]:
        logging.debug(f'Overshot with {next_x=} {target_x=} {next_y=} {target_y=}')
        return False

    # We have more to travel
    return fire_probe(next_x, next_y, xv, yv, target_x, target_y)


def test1():
    #logging.basicConfig(level=logging.DEBUG)

    target_xx = (20,30,)
    target_yy = (-10,-5,)
    initial_velocity = []
    
    for xx in range(-100,100,1):
        for yy in range(-100,100,1):           
            result = fire_probe(0,0,xx,yy,target_xx,target_yy)
            if result:
                initial_velocity.append((xx, yy,))
    
    print(initial_velocity, len(initial_velocity))


# Solution is brute force. I cannot think of a better way to handle this !!
def solution2():

    target_xx = (85,145,)
    target_yy = (-163,-108,)
    initial_velocity = []
    
    for xx in range(-200,200,1):
        for yy in range(-200,200,1):           
            result = fire_probe(0,0,xx,yy,target_xx,target_yy)
            if result:
                initial_velocity.append((xx, yy,))
    
    print(initial_velocity)
    print(f'{target_xx=} {target_yy=} {len(initial_velocity)} Expected=5644')
   

if __name__ == '__main__':
    #test1()
    solution2()
    




    
