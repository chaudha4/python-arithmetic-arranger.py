
# https://adventofcode.com/2021/day/20

def load(file='./adventofcode/20-trench-map-1.txt'):
    lines = []
    with open(file) as f:
        lines = f.read().split("\n\n")

    assert len(lines) == 2, f'Expected Two entries. First one should be Rules and next one should be the image. Got {lines=}'
    image_rules = lines[0]

    input_image = []
    for row in lines[1].split("\n"):
        rr = []
        for cols in row:
            rr.append(cols)
        input_image.append(rr)
    
    return image_rules, input_image


def enlarge(input_image, times=1):

    assert type(input_image) == list
    assert len(input_image) > 0
    for xx in input_image:
        assert type(xx) == list, f'Must be two dimension. Found Error at {xx=}'

    rcount = len(input_image[0])
    ccount = len(input_image)

    # Safe to expand by just the current number of rows.
    toadd = rcount * times

    # Create Filler rows for Top and bottom
    filler_col = ['.'  for _ in range(toadd*2 + ccount)]
    
    expanded_image = []
    
    # Fill empty rows above
    for _ in range(toadd):
        expanded_image.append(filler_col)

    for rr in input_image:
        # Append cols before and after.
        cols = []
        for _ in range(toadd):
            cols.append('.')
        
        for cc in rr:
            cols.append(cc)

        for _ in range(toadd):
            cols.append('.')

        expanded_image.append(cols)

    # Fill empty rows below
    for _ in range(toadd):
        expanded_image.append(filler_col)

    print(f'Before Expansion size was {rcount}x{rcount}. After expanding {times} times, size is {len(expanded_image)}x{len(expanded_image[0])}')
    
    return expanded_image


def enhance_image(input_image, image_rules):

    output_image = []

    for rrIdx, rr in enumerate(input_image):
        col = []
        maxrl = len(input_image)
        #print(f'{rrIdx=} {rr=}')
        for ccIdx, cc in enumerate(rr):
            #print(f'{ccIdx=} {cc=} {maxrl=}')
            binStr = ''
            binValid = True # Track edge cases. Their values saty unchanged.
            maxcl = len(rr)
            for jj in range(rrIdx-1,rrIdx+2):
                for kk in range(ccIdx-1,ccIdx+2):
                    #print(f'{jj=} {kk=} {binStr=} {maxcl=}')
                    if jj < 0 or jj >= maxrl or kk < 0 or kk >= maxcl:
                        binValid = False
                    else:
                        if input_image[jj][kk] == '.':
                            binStr = binStr + '0'
                        else:
                            binStr = binStr + '1'
                    


            if binValid:
                decValue  = int(binStr,2)
                #print(f'{binStr=} {binValid=} {decValue=} {ccIdx=} {cc=} {maxrl=} {maxcl=} {image_rules[decValue]=}')
                col.append(image_rules[decValue])
            else:
                # This is the edge case. Image size is infinite, so we just assume anything outside must have the same value as this pixel.
                if cc == '.':
                    # All my neighbours must also be the same as me. If they are all "." then the sum will be zero.
                    col.append(image_rules[0])
                else:
                    # All my neighbours must also be the same as me. If they are all "#" then the sum will be max.
                    col.append(image_rules[-1])
        
        output_image.append(col)
                       
                        
    return output_image

def test1():
    image_rules, input_image = load()
    new_image = enlarge(input_image)
    for rr in new_image:
        print(rr)

    print("\n\n")
    ei = enhance_image(new_image, image_rules)
    for rr in ei:
        print(rr)    

    print("\n\n")
    
    ei = enhance_image(ei, image_rules)
    for rr in ei:
        print(rr)

    print("\n\n")
    count = 0
    for rr in ei:
        for cc in rr:
            if cc == '#':
                count = count + 1

    print(f'{count=} Expected=35')


def test2():
    image_rules, input_image = load()
    new_image = enlarge(input_image, 50)
    
    ei = new_image
    for _ in range(50):
        ei = enhance_image(ei, image_rules)

    count = 0
    for rr in ei:
        for cc in rr:
            if cc == '#':
                count = count + 1

    print(f'{count=} Expected=3351')

def getHashCount(image):
    count = 0
    for rr in image:
        for cc in rr:
            if cc == '#':
                count = count + 1
    return count    

def solution1():
    image_rules, input_image = load('./adventofcode/20-trench-map-2.txt')
    new_image = enlarge(input_image)
    ei = enhance_image(new_image, image_rules)
    ei = enhance_image(ei, image_rules)
    print(f'Count={getHashCount(ei)}  Expected=5259')


def solution2():
    image_rules, input_image = load('./adventofcode/20-trench-map-2.txt')
    new_image = enlarge(input_image, 5)

    ei = new_image
    for ii in range(50):
        ei = enhance_image(ei, image_rules)
        print(f'After iteration {ii}, count of # is {getHashCount(ei)}')

    print(f'Count={getHashCount(ei)} Expected=15287')

#test1()
solution1()

#test2()
#solution2()
