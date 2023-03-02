# https://adventofcode.com/2021/day/22#part2

'''
The part1 solution will not scale. I tried to optimize it but could not get it run. Ran out of ideas and then looked up on how
others have solved it.

One solution ppropsed was to treat the coordinates as cuboid and the volume of the cuboid will represent the points that are "on".
This will scale since volume calculation is simple. The trick was to look for overlaps between cuboids and not double count the
overlaps. Apply overlap principle for Cuboids representing "off" points.

Another solution would be to split cuboids into smaller ones and discard the overlapped ones. Also discard the "off" ones. I did
not try this approach since it will also be somewhat slow due to numerous small cuboids.

My solution is really inspired by https://gist.github.com/joshbduncan/175c4b42fc9cf3d543dbee42f5fbd8ee

'''


from collections import namedtuple, defaultdict

Point = namedtuple("Point", ["x", "y", "z"])

class Cuboid:

    def __init__(self, point1: Point, point2: Point) -> None:
        self.p1  = point1
        self.p2  = point2
        pass

    def __repr__(self) -> str:
        return f'Cuboid[({self.p1.x},{self.p1.y},{self.p1.z}),({self.p2.x},{self.p2.y},{self.p2.z}),{self.volume}]'
    
    # Need this to use Cuboid as a Key in dictionary.
    def __eq__(self, __o: object) -> bool:
        if self.p1.x != __o.p1.x:
            return False
        if self.p1.y != __o.p1.y:
            return False
        if self.p1.z != __o.p1.z:
            return False
        if self.p2.x != __o.p2.x:
            return False
        if self.p2.y != __o.p2.y:
            return False
        if self.p2.z != __o.p2.z:
            return False

        return True

    # Need this to use Cuboid as a Key in dictionary.
    def __hash__(self) -> int:
        return hash(((self.p1.x,self.p1.y,self.p1.z),(self.p2.x,self.p2.y,self.p2.z),))    
    

    # Make volume a property so that it can be accessed as a variable rather than a function. 
    @property
    def volume(self) -> int:
        return  (abs(self.p2.x - self.p1.x) + 1) * \
                (abs(self.p2.y - self.p1.y) + 1) * \
                (abs(self.p2.z - self.p1.z) + 1) 

    @property
    def valid(self) -> bool:
        if  self.p1.x <= self.p2.x and \
            self.p1.y <= self.p2.y and \
            self.p1.z <= self.p2.z:
            return True
        return False


def overlap(c1: Cuboid, c2: Cuboid) -> Cuboid:

    # Create a new Cuboid that represents the overlap of c1 and c2. If it is valid cuboid, then there is an overlap else no overlap.
    p1 = Point(max(c1.p1.x, c2.p1.x), max(c1.p1.y, c2.p1.y), max(c1.p1.z, c2.p1.z))
    p2 = Point(min(c1.p2.x, c2.p2.x), min(c1.p2.y, c2.p2.y), min(c1.p2.z, c2.p2.z))

    c = Cuboid(p1, p2)
    return c


def load_file(file: str) -> list:
    
    data = []

    with open(file) as f:
        lines = f.read().split('\n')

        for line in lines:
            if len(line) == 0 or line[0] == "#":
                #Ignore black lines or commented lines
                continue
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

            p1 = Point(x1,y1,z1)
            p2 = Point(x2,y2,z2)

            data.append((op, Cuboid(p1, p2),))
    
    return data

def getCount(myfile: str = 'adventofcode/22-input-1.txt') -> int:
    # myfile = 'adventofcode/22-input-1.txt'
    # myfile = 'adventofcode/temp.txt'

    data = load_file(myfile)

    # Key is Cuboid, Value is a number representing the number of +ve or -ve occurances
    working_list = defaultdict(int)

    for op, cub1 in data:
        temp_results = defaultdict(int)
        for cub2, val2 in working_list.items():
            overlapped_cuboid = overlap(cub1, cub2)
            # print(f'Overlapped Cuboid is {overlapped_cuboid}')
            if overlapped_cuboid.valid:
                # Reduce the overlapped count since it will be double counted. You cannot decrement by 1 since all previous 
                # overlaps are counted again in this cycle + a few more.
                temp_results[overlapped_cuboid] = temp_results[overlapped_cuboid] - val2

        # After processing current cuboid, add it to the working list so that it gets compared to all others that follow.
        if op == "on":
            working_list[cub1] += 1

        for k, v in temp_results.items():
            working_list[k] += v


    # print(f'{working_list=}')

    volume = 0

    for cub, count in working_list.items():
        adjust = cub.volume * count
        volume += adjust
        #print(f'{cub} {count} {adjust} {volume}')
    
    return volume


def solution1():
    file = 'adventofcode/22-input.txt'
    num_of_points_on = getCount(file)
    print(f'Day 22: Reactor Reboot - Part 2. After running the above reboot steps, {num_of_points_on} cubes are on.')
    assert num_of_points_on == 1236463892941356

#test1()
solution1()


    