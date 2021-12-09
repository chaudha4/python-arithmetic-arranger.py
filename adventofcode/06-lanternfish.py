#https://adventofcode.com/2021/day/6/

inputdata = [2,1,1,1,1,1,1,5,1,1,1,1,5,1,1,3,5,1,1,3,1,1,3,1,4,4,4,5,1,1,1,3,1,3,1,1,2,2,1,1,1,5,1,1,1,5,2,5,1,1,2,1,3,3,5,1,1,4,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,4,1,5,1,2,1,1,1,1,5,1,1,1,1,1,5,1,1,1,4,5,1,1,3,4,1,1,1,3,5,1,1,1,2,1,1,4,1,4,1,2,1,1,2,1,5,1,1,1,5,1,2,2,1,1,1,5,1,2,3,1,1,1,5,3,2,1,1,3,1,1,3,1,3,1,1,1,5,1,1,1,1,1,1,1,3,1,1,1,1,3,1,1,4,1,1,3,2,1,2,1,1,2,2,1,2,1,1,1,4,1,2,4,1,1,4,4,1,1,1,1,1,4,1,1,1,2,1,1,2,1,5,1,1,1,1,1,5,1,3,1,1,2,3,4,4,1,1,1,3,2,4,4,1,1,3,5,1,1,1,1,4,1,1,1,1,1,5,3,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,5,1,4,4,1,1,1,1,1,1,1,1,3,1,3,1,4,1,1,2,2,2,1,1,2,1,1]



def fish_after(fish_age, days):
  
    # save the age as the first entry. Children will be appened to this array.
    fish = [fish_age]
    
    for dd in range(days):
        num2add = 0
        for idx, ff in enumerate(fish):
            if (ff == 0):
                num2add = num2add + 1
                fish[idx] = 6
            else:
                fish[idx] = fish[idx] - 1
        while (num2add > 0):
            fish.append(8)
            num2add = num2add - 1

    return fish


# This will scale upto 180 days or so. AFter that, it runs out of memory.
def puzzle1(days=80):
    tot = 0
    for ff in inputdata:
        tot = tot + len(fish_after(ff, days))
    print(tot)


def puzzle2(days=256):
      
    # Cache the number of fish after N days - Index is the age of the fist at start.
    # So one fish of age 2 will become lkup[2] fish after N days. 
    lkup = []

    # Cache the age of each fish as it will look after N days. Index is the current age.
    # A fish of age 0 today will have many children after N days. And their age would be lkup1[0]
    lkup1 = []

    # Number of day to build a cache. Then the cache can be reused to go further.
    halfdays = int(days/2)

    # Time to build the cache. Fish can be 0 days old to a max of 8 days old.
    for aa in range(9):
        res = fish_after(aa, halfdays)
        lkup.append(len(res))
        lkup1.append(res)
        
    #print(lkup)
    #print(lkup1)

    # arr1 will hold the new snapshot of fish age after 128 days.
    arr1 = []
    total = 0
    for aa in inputdata:
        total = total + lkup[aa]
        arr1.append(lkup1[aa])

    print(f'After {halfdays} days: {total}')

    # We are half way thru. Now we know how the fish array looks after 128 days. We also know
    # how many more fish will get added in next 128 days by using our cache that we built above.
    
    total1 = 0  # We can ignore the old total since the new array already has that total in it.

    for batch in arr1:
        #print(batch)
        for b in batch:
            total1 = total1 + lkup[b]

    print(f'After {days} days: {total1}')


if __name__ == "__main__":

    #puzzle1()
    #puzzle2(80)
    puzzle2()

