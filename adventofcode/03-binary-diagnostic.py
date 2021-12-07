# https://adventofcode.com/2021/day/3

def func1():

    msb = []

    with open("./adventofcode/03-binary-diagnostic.txt") as f:
        nums = f.read().split()

        cnt0 = []
        cnt1 = []
        for bits in nums:
            for idx, bit in enumerate(bits):
                try:
                    test = cnt0[idx]
                except:
                    cnt0.append(0)

                try:
                    test = cnt1[idx]
                except:
                    cnt1.append(0)

                if ( bit == '0'):
                    cnt0[idx] = cnt0[idx] + 1
                else:
                    cnt1[idx] = cnt1[idx] + 1

        print(cnt0, cnt1)
        
        gamma_rate = ""
        epsilon_rate = ""
        for msb, lsb in zip(cnt0, cnt1):
            print(msb, lsb)
            if (msb > lsb):
                gamma_rate = gamma_rate + "1"
                epsilon_rate = epsilon_rate + "0"
            else:
                gamma_rate = gamma_rate + "0"
                epsilon_rate = epsilon_rate + "1"
        
        print(gamma_rate, epsilon_rate)
        gr = int(gamma_rate, 2)
        er = int(epsilon_rate, 2)
        
        print(gr, er)

        power_consumption = gr * er
        print(power_consumption)
        return power_consumption




"""
determine the most common value (0 or 1) in the current bit position, 
and keep only numbers with that bit in that position. If 0 and 1 are 
equally common, keep values with a 1 in the position being considered.
"""

def mcv(diag_list, bit_pos):

    num0 = []
    num1 = []
    for nn in diag_list:
        if (nn[bit_pos] == '0'):
            num0.append(nn)
        else:
            num1.append(nn)

    print("List of Bit 0 at ", bit_pos, num0[:10:])
    print("List of Bit 1 at ", bit_pos, num1[:10:])

    len0 = len(num0)
    len1 = len(num1)

    if (len1 >= len0):
        return len1, num1
    return len0, num0
     

"""
determine the least common value (0 or 1) in the current bit position, and keep 
only numbers with that bit in that position. If 0 and 1 are equally common, 
keep values with a 0 in the position being considered.
"""

def lcv(diag_list, bit_pos):

    num0 = []
    num1 = []
    for nn in diag_list:
        if (nn[bit_pos] == '0'):
            num0.append(nn)
        else:
            num1.append(nn)

    print("List of Bit 0 at ", bit_pos, num0[:10:])
    print("List of Bit 1 at ", bit_pos, num1[:10:])

    len0 = len(num0)
    len1 = len(num1)

    if (len0 <= len1):
        return len0, num0
    return len1, num1
     



def func2():
    with open("./adventofcode/03-binary-diagnostic.txt") as f:
        data = f.read().split()

        sz = len(data[0])
        
        #oxygen generator rating
        temp = data
        for ii in range(sz):
            lenx, tempx = mcv(temp, ii)
            temp = tempx

            if (lenx == 1):
                break
            
        print("oxygen generator rating", temp)
        ogr = int(str(*temp), 2)

        #CO2 scrubber rating
        temp = data
        for ii in range(sz):
            lenx, tempx = lcv(temp, ii)
            temp = tempx

            if (lenx == 1):
                break
            
        print("CO2 scrubber rating", temp)        
        csr = int(str(*temp), 2)

        #life support rating
        lsr = ogr * csr

        print(ogr, csr, lsr)


#func1()
func2()