
x1, y1, x2, y2 = 9,7,9,9

xstep, ystep = 1, 1

if (x1 > x2):
    xstep = -1

if (y1 > y2):
    ystep = -1

for xx, yy in zip(range(x1, x2, xstep), range(y1, y2, ystep)):
    print(xx, yy)


