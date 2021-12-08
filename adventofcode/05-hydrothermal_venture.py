import numpy as np

class hydrovent:

    def __repr__(self) -> str:
        ret = "\tHydrothermal Venture\t\n\t--------------------\t\n"
        ret = ret + np.str(self.points) + "\n\n"
        return ret

    def __init__(self) -> None:
        self.points = np.zeros((1000,1000))


    def addLine(self, C1, C2):
        x1, y1 = C1
        x2, y2 = C2
    

        # if X coordinates are same it is a horizontal line
        if (x1 == x2):
            # Move horizontally
            ystep = 1
            if (y1 > y2):
                ystep = -1
            for yy in range(y1, y2, ystep):
                self.points[x1, yy] = self.points[x1, yy] + 1
            # range will miss the last coordinate
            self.points[x2, y2] = self.points[x2, y2] + 1
        elif (y1 == y2):
            # Move vertically
            xstep = 1
            if (x1 > x2):
                xstep = -1
            
            for xx in range(x1, x2, xstep):
                self.points[xx, y1] = self.points[xx, y1] + 1
            
            # range will miss the last coordinate
            self.points[x2, y2] = self.points[x2, y2] + 1
        else:
            # Diagonal line
            xstep, ystep = 1, 1
            if (x1 > x2):
                xstep = -1
            if (y1 > y2):
                ystep = -1

            # This will handle diagonal lines.
            for xx, yy in zip(range(x1, x2, xstep), range(y1, y2, ystep)):
                self.points[xx,yy] = self.points[xx,yy] + 1
            
            # range will miss the last coordinate
            self.points[x2,y2] = self.points[x2,y2] + 1            

    def count(self, limit):
        return self.points[self.points > limit].shape[0]


def load(filename):
    data = []
    with open(filename, "r") as f:
        lines = f.read().split("\n")
        for l in lines:
            start_end = l.split(" -> ")
            #print(start_end)
            temp1 = start_end[0].split(",")
            temp2 = start_end[1].split(",")
            coordinates_start = (int(temp1[0]), int(temp1[1]))
            coordinates_end = (int(temp2[0]), int(temp2[1]))
            
            data.append((coordinates_start, coordinates_end))
    
    return data


if __name__ == "__main__":

    data = load("/home/chaudha4/Projects/Python-Projects/adventofcode/05-hydrothermal_venture.txt")
    hv = hydrovent()

    for d in data:   
        hv.addLine(d[0], d[1])

    print(hv)
    # How many line intersections
    print(hv.count(1))




