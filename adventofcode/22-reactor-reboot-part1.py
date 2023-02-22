# https://adventofcode.com/2021/day/22


from collections import namedtuple


def load(file='adventofcode/22-input-1.txt'):

    Operation = namedtuple("Operation", ["op", "x1", 'x2', 'y1', "y2", "z1", 'z2'])
    ret = []
    with open(file) as f:
        lines = f.read().split('\n')

        for line in lines:
            op, vals = line.split()
            xx, yy, zz = vals.split(",")
            xx = xx[2:]
            yy = yy[2:]
            zz = zz[2:]

            x1, x2 = xx.split("..")
            x1, x2 = int(x1), int(x2)

            y1, y2 = yy.split("..")
            y1, y2 = int(y1), int(y2)

            z1, z2 = zz.split("..")
            z1, z2 = int(z1), int(z2)

            #dontAdd = False


            # considering only cubes in the region x=-50..50,y=-50..50,z=-50..50,
            
            if  (x1 < -50 and x2 < -50) or (x1 > 50 and x2 > 50) or \
                (y1 < -50 and y2 < -50) or (y1 > 50 and y2 > 50) or \
                (z1 < -50 and z2 < -50) or (z1 > 50 and z2 > 50):
                continue

            if x1 < -50:
                x1 = -50

            if x2 > 50:
                x2 = 50

            if y1 < -50:
                y1 = -50

            if y2 > 50:
                y2 = 50     

            if z1 < -50:
                z1 = -50

            if z2 > 50:
                z2 = 50     

            ret.append(Operation(op, x1, x2, y1, y2, z1, z2))

    return ret

def reboot(operations):

    onList = set()

    for o in operations:
        for x in range(o.x1, o.x2+1):
            for y in range(o.y1, o.y2+1):
                for z in range(o.z1, o.z2+1):
                    if o.op == "on":
                        onList.add((x,y,z,))
                    elif o.op == "off":
                        if (x,y,z,) in onList:
                            onList.remove((x,y,z))

    return len(onList)

def test1():
    opers = load()
    count = reboot(opers)
    assert count == 590784

def solution1():
    opers = load("adventofcode/22-input-part1.txt")
    count = reboot(opers)
    assert count == 615700



test1()
solution1()

    