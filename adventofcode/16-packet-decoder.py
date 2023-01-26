#https://adventofcode.com/2021/day/16

from collections import deque


def hex_to_bin_str(hex_str):

    val = int(hex_str, 16)
    bin_str = str(bin(val))[2:] # remove 0b
    
    #pad zeros. Must be a multiple of 4.
    l = len(bin_str)
    x = l % 4
    y = l // 4
   
    pd = 0
    if x > 0: # need padding
        pd = (4* (y+1)) - (l)
    
    bin_str = bin_str.zfill(l+pd)

    print()
    print('*' * len(hex_str))
    #print(f'{l=} {x=} {y=} {pd=} {bin_str=}')
    print(hex_str)
    print('*' * len(hex_str))

    return bin_str   


verSum = 0

# Test stage 1

def parse(p):
    
    global verSum
    print(f"\n\n{verSum=}")
    if len(p) == 0:
        return
    
    ver = int(p[0:3], 2)
    typ = int(p[3:6], 2)

    verSum = verSum + ver

    print(f'{ver=} {typ=} {p=}')

    ii = 6
    if typ == 4:
        # Literal Packets
        next5 = p[ii:ii+5]
        numStr = ""
        while len(next5) == 5:
            print(f'{next5=} {ii=}')
            numStr = numStr + next5[1:]
            ii = ii + 5 # Get ready for next iteration
            if next5[0] == '0':
                break
                
            next5 = p[ii:ii+5]

        numInt = int(numStr,2)   # length of the sub-packets
        print(f'{numInt=} {ii=} {p[ii:]} {n=}')
        if n > 0:        
            parse(p[ii:], n:= n-1)
    else:
        # Oper Packets       
        ltid = int(p[ii], 2)
        ii = ii + 1 
        
        if ltid == 0: # 0 means accumulate next 15 bits, 1 means 11 bits.
            nextGrp = p[ii: ii+15] # 15 bits contain the length of the sub-packets
            ii = ii+15
            len_of_all_subpkts = int(nextGrp, 2)
            sub_pkt_grp = p[ii: ii+len_of_all_subpkts]
            ii = ii + len_of_all_subpkts
            print(f'Oper Packet {ver=} {typ=} {ltid=} {len_of_all_subpkts=} {sub_pkt_grp=}')            
            if n > 0:
                parse(sub_pkt_grp, n:= n-1)
            #parse(p[ii:])
        else:
            nextGrp = p[ii:ii+11]
            ii = ii+11
            num_of_pkts = int(nextGrp, 2)
            print(f'Oper p {ver=} {typ=} {ltid=} {num_of_pkts=} ')
            for kk in range(num_of_pkts):
                if n > 0:
                    ii = parse(p[ii:], num_of_pkts)  # Bug is here...
                #process_pkt(sub_pkt_grp[ii*11:(ii*11)+11]) # recursion
                #pktq.append(sub_pkt_grp[ii*11:(ii*11)+11])
            #parse(p[ii:])

    #parse(p[ii:])
    return ii  # Return the index of where the parsing stopped


def parse1(p):
    
    global verSum
    print(f"\n{verSum=} Processing {p=}")
    if len(p) == 0:
        return
    
    ver = int(p[0:3], 2)
    typ = int(p[3:6], 2)

    verSum = verSum + ver

    #print(f'{ver=} {typ=} {p=}')

    ii = 6
    if typ == 4:
        # Literal Packets
        next5 = p[ii:ii+5]
        numStr = ""
        while len(next5) == 5:
            print(f'{next5=} {ii=}')
            numStr = numStr + next5[1:]
            ii = ii + 5 # Get ready for next iteration
            if next5[0] == '0':
                break
                
            next5 = p[ii:ii+5]

        numInt = int(numStr,2)   # length of the sub-packets
        print(f'Literal Packet processed {numInt=} {ii=} remaining packet {p[ii:]=}')
        return p[ii:]
    else:
        # Oper Packets       
        ltid = int(p[ii], 2)
        ii = ii + 1 
        
        if ltid == 0: # 0 means accumulate next 15 bits, 1 means 11 bits.
            nextGrp = p[ii: ii+15] # 15 bits contain the length of the sub-packets
            ii = ii+15
            len_of_all_subpkts = int(nextGrp, 2)
            sub_pkt_grp = p[ii: ii+len_of_all_subpkts]
            ii = ii + len_of_all_subpkts
            print(f'Oper Packet Length based {ver=} {typ=} {ltid=} {len_of_all_subpkts=} {sub_pkt_grp=}')
            leftOverPacket = p[ii:] # subpackets will be processed. Everything else should be returned back.
            p = sub_pkt_grp
            while len_of_all_subpkts > 0:                           
                lb4 = len(p)
                p = parse1(p)
                laftr = len(p)
                len_of_all_subpkts = len_of_all_subpkts - (lb4 - laftr)
                print(f'Oper Packet Length next packet {lb4=} {laftr=} {ii=} {len_of_all_subpkts=}')
            return leftOverPacket

        else:
            nextGrp = p[ii:ii+11]
            ii = ii+11
            num_of_pkts = int(nextGrp, 2) 
            p = p[ii:]
            print(f'Oper packet count based {ver=} {typ=} {ltid=} {num_of_pkts=} {p=}')
            for _ in range(num_of_pkts):
                lb4 = len(p)
                p = parse1(p)
                laftr = len(p)
                ii = lb4 - laftr
                print(f'Oper Packet count processing {lb4=} {laftr=} {ii=} next is {p=}')
            return p

    #parse(p[ii:])
    raise AssertionError(f'Unreachable Code - Should have returned before')



def parseWithLength(p, l=0):
    
    global verSum
    print(f"\n\n{verSum=}")
    if len(p) == 0:
        return
    
    ver = int(p[0:3], 2)
    typ = int(p[3:6], 2)

    verSum = verSum + ver

    print(f'parseWithLength - {ver=} {typ=} {p=} {l=}')

    while l > 0:
        l = l - parse(p)
        print

    ii = 6
    if typ == 4:
        # Literal Packets
        next5 = p[ii:ii+5]
        numStr = ""
        while len(next5) == 5:
            print(f'{next5=} {ii=}')
            numStr = numStr + next5[1:]
            ii = ii + 5 # Get ready for next iteration
            if next5[0] == '0':
                break
                
            next5 = p[ii:ii+5]

        numInt = int(numStr,2)   # length of the sub-packets
        print(f'{numInt=} {ii=} {p[ii:]} {n=}')
        if n > 0:        
            parse(p[ii:], n:= n-1)
    else:
        # Oper Packets       
        ltid = int(p[ii], 2)
        ii = ii + 1 
        
        if ltid == 0: # 0 means accumulate next 15 bits, 1 means 11 bits.
            nextGrp = p[ii: ii+15] # 15 bits contain the length of the sub-packets
            ii = ii+15
            len_of_all_subpkts = int(nextGrp, 2)
            sub_pkt_grp = p[ii: ii+len_of_all_subpkts]
            ii = ii + len_of_all_subpkts
            print(f'Oper Packet {ver=} {typ=} {ltid=} {len_of_all_subpkts=} {sub_pkt_grp=}')            
            if n > 0:
                parse(sub_pkt_grp, n:= n-1)
            #parse(p[ii:])
        else:
            nextGrp = p[ii:ii+11]
            ii = ii+11
            num_of_pkts = int(nextGrp, 2)
            print(f'Oper p {ver=} {typ=} {ltid=} {num_of_pkts=} ')
            for kk in range(num_of_pkts):
                if n > 0:
                    ii = parse(p[ii:], num_of_pkts)  # Bug is here...
                #process_pkt(sub_pkt_grp[ii*11:(ii*11)+11]) # recursion
                #pktq.append(sub_pkt_grp[ii*11:(ii*11)+11])
            #parse(p[ii:])

    #parse(p[ii:])
    return ii  # Return the index of where the parsing stopped


sampleHex = [
    ('8A004A801A8002F478', 16),
    ('620080001611562C8802118E34', 12),
    ('C0015000016115A2E0802F182340', 23),
    ('A0016C880162017C3686B18A3D4780', 31),
    ('8054F9C95F9C1C973D000D0A79F6635986270B054AE9EE51F8001D395CCFE21042497E4A2F6200E1803B0C20846820043630C1F8A840087C6C8BB1688018395559A30997A8AE60064D17980291734016100622F41F8DC200F4118D3175400E896C068E98016E00790169A600590141EE0062801E8041E800F1A0036C28010402CD3801A60053007928018CA8014400EF2801D359FFA732A000D2623CADE7C907C2C96F5F6992AC440157F002032CE92CE9352AF9F4C0119BDEE93E6F9C55D004E66A8B335445009E1CCCEAFD299AA4C066AB1BD4C5804149C1193EE1967AB7F214CF74752B1E5CEDC02297838C649F6F9138300424B9C34B004A63CCF238A56B71520142A5A7FC672E5E00B080350663B44F1006A2047B8C51CC80286C0055253951F98469F1D86D3C1E600F80021118A124261006E23C7E8260008641A8D51F0C01299EC3F4B6A37CABD80252211221A600BC930D0057B2FAA31CDCEF6B76DADF1666FE2E000FA4905CB7239AFAC0660114B39C9BA492D4EBB180252E472AD6C00BF48C350F9F47D2012B6C014000436284628BE00087C5D8671F27F0C480259C9FE16D1F4B224942B6F39CAF767931CFC36BC800EA4FF9CE0CCE4FCA4600ACCC690DE738D39D006A000087C2A89D0DC401987B136259006AFA00ACA7DBA53EDB31F9F3DBF31900559C00BCCC4936473A639A559BC433EB625404300564D67001F59C8E3172892F498C802B1B0052690A69024F3C95554C0129484C370010196269D071003A079802DE0084E4A53E8CCDC2CA7350ED6549CEC4AC00404D3C30044D1BA78F25EF2CFF28A60084967D9C975003992DF8C240923C45300BE7DAA540E6936194E311802D800D2CB8FC9FA388A84DEFB1CB2CBCBDE9E9C8803A6B00526359F734673F28C367D2DE2F3005256B532D004C40198DF152130803D11211C7550056706E6F3E9D24B0', 0)
]


for testval, expAns in sampleHex:
    verSum = 0
    parse1(hex_to_bin_str(testval))
    print(f'{verSum=} {expAns=}')


def process_pkt_group(p, q):

    packet = p.val

    ver = int(packet[0:3], 2)
    typ = int(packet[3:6], 2)
    print(f'{ver=} {typ=} {packet=}')

    if typ == 4:
        return process_literal_pkt(p, q)
    else:
        return process_oper_pkt(p, q)


def process_literal_pkt(p, pktq):

    packet = p.val
    ver = int(packet[0:3], 2)
    typ = int(packet[3:6], 2)
    print(f'Literal Packet {ver=} {typ=} {packet=}')
    
    assert typ == 4, "Literal Packet type must be 4"

    currIndex = 6  # Already read ver and type.
    
    #print(ver, typ, rem)

    # Read 5 bits in groups till we run out. Save the index of where we stop.

    next5 = packet[currIndex:currIndex+5]
    currIndex = currIndex+5
    numStr = ""

    while len(next5) == 5:
        print(f'{next5=}')
        numStr = numStr + next5[1:]
        currIndex = currIndex+5 # Get ready for next iteration
        if next5[0] == '0':
            break
               
        next5 = packet[currIndex:currIndex+5]

    numInt = int(numStr,2)
    print(f'{numInt=} {currIndex=}')
    return numInt
    

def process_oper_pkt(packet, pktq):

    ver = int(packet[0:3], 2)
    typ = int(packet[3:6], 2)
    
    assert typ != 4, "Operator Packet type must NOT be 4"
    
    # length type ID - 0 means accumulate next 15 bits, 1 means 11 bits.
    ltid = int(packet[6], 2)
    
    
    if ltid == 0:
        nextGrp = packet[7:22] # number of bits in the sub-packets.
        len_of_all_subpkts = int(nextGrp, 2)
        sub_pkt_grp = packet[22: 22+len_of_all_subpkts]
        #Each subpacket is 11 bits except the last one that will have the leftover bits 

        num_of_pkts = len_of_all_subpkts // 11
        extra = len_of_all_subpkts % 11

        print(f'Oper Packet {ver=} {typ=} {ltid=} {len_of_all_subpkts=} {num_of_pkts=} {sub_pkt_grp=}')
        pktq.append(sub_pkt_grp)

    else:
        nextGrp = packet[7:18]
        num_of_pkts = int(nextGrp, 2)
        sub_pkt_grp = packet[22: 22+(11*num_of_pkts)]

        print(f'Oper Packet {ver=} {typ=} {ltid=} {num_of_pkts=} {sub_pkt_grp=}')
        for ii in range(num_of_pkts):
            #process_pkt(sub_pkt_grp[ii*11:(ii*11)+11]) # recursion
            pktq.append(sub_pkt_grp[ii*11:(ii*11)+11])


def hex_to_bin_string(hex_str):

    val = int(hex_str, 16)
    bin_str = str(bin(val))

    #pad zeros. Must be a multiple of 4.

    x = len(bin_str) % 4
    y = len(bin_str) // 4
    pad = 0
    if y > 0:
        pad = len(bin_str) * (x+1) - len(bin_str) * (x)
    

    #print(bin_str[2:])
    return bin_str[2:]   # remove 0b and send the rest


def hex_to_bin(hex_str):

    bin_str = ""
    for hh in hex_str:
        val = int(hh, 16)
        bin_str = bin_str + bin(val)[2:].zfill(4)
    
    #print(bin_str)
    return bin_str

 