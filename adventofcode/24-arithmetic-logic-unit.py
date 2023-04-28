# https://adventofcode.com/2021/day/24

from collections import defaultdict

def load1(file:str ='adventofcode/24-test-data.txt') -> list:

    rows = None
    with open(file) as f:
        rows = f.read().strip().split('\n')
    return rows


def load_rules(file:str ='adventofcode/24-test-data.txt') -> defaultdict:

    rows = None
    with open(file) as f:
        rows = f.read().strip().split('\n')
    
    rule_dict = defaultdict(list)
    rule_idx = -1
    for row in rows:
        op = row.split(' ')
        if op[0] == "inp":
            # New rule
            rule_idx += 1
        rule_dict[rule_idx].append(op)

    return rule_dict

def calculate(model_num: int):

    operlist = load1()
    results = defaultdict(int)

    model_num_str = str(model_num)
    inp_index = 0

    for oper in operlist:
        oper = oper.split(' ')

        if oper[0] == 'inp':
            num = int(model_num_str[inp_index])
            results[oper[1]] = num
            inp_index += 1
            # print(f"{results=} {num=}")
        elif oper[0] == 'eql':
            lhs = oper[1]
            rhs = oper[2]
            if rhs.isnumeric() or rhs[0] == '-':
                results[lhs] = int(results[lhs] == int(rhs))
            else:
                results[lhs] = int(results[lhs] == results[rhs])            
        elif oper[0] == 'add':
            lhs = oper[1]
            rhs = oper[2]
            if rhs.isnumeric() or rhs[0] == '-':
                results[lhs] += int(rhs)
            else:
                results[lhs] += results[rhs]     
        elif oper[0] == 'div':
            lhs = oper[1]
            rhs = oper[2]
            if rhs.isnumeric() or rhs[0] == '-':
                results[lhs] //=  int(rhs)
            else:
                results[lhs] //= results[rhs]      
        elif oper[0] == 'mod':
            lhs = oper[1]
            rhs = oper[2]
            if rhs.isnumeric() or rhs[0] == '-':
                results[lhs] //= int(rhs)
            else:
                results[lhs] //= results[rhs]      
        elif oper[0] == 'mul':
            lhs = oper[1]
            rhs = oper[2]
            if rhs.isnumeric() or rhs[0] == '-':
                results[lhs] *= int(rhs)
            else:
                results[lhs] *= results[rhs]
        else:
            assert False, f'Unsupported Operation {oper}'

    return results

def apply_rule(w_input: int, z_input: int, ruled_id: int, rules: defaultdict, cache :dict={}):

    key = (w_input, z_input, ruled_id,)

    #print(f'{key=} {cache=}')
    if key in cache:
        print(f'Returning from cache {key=} {cache[key]=}')
        return cache[key]
    
    results = defaultdict(int)
    results['w'] = w_input
    results['z'] = z_input

    for oper in rules[ruled_id]:
        if oper[0] == 'inp':
            pass
        elif oper[0] == 'eql':
            lhs = oper[1]
            rhs = oper[2]
            if rhs.isnumeric() or rhs[0] == '-':
                results[lhs] = int(results[lhs] == int(rhs))
            else:
                results[lhs] = int(results[lhs] == results[rhs])            
        elif oper[0] == 'add':
            lhs = oper[1]
            rhs = oper[2]
            if rhs.isnumeric() or rhs[0] == '-':
                results[lhs] += int(rhs)
            else:
                results[lhs] += results[rhs]     
        elif oper[0] == 'div':
            lhs = oper[1]
            rhs = oper[2]
            if rhs.isnumeric() or rhs[0] == '-':
                results[lhs] //=  int(rhs)
            else:
                results[lhs] //= results[rhs]      
        elif oper[0] == 'mod':
            lhs = oper[1]
            rhs = oper[2]
            if rhs.isnumeric() or rhs[0] == '-':
                results[lhs] //= int(rhs)
            else:
                results[lhs] //= results[rhs]      
        elif oper[0] == 'mul':
            lhs = oper[1]
            rhs = oper[2]
            if rhs.isnumeric() or rhs[0] == '-':
                results[lhs] *= int(rhs)
            else:
                results[lhs] *= results[rhs]
        else:
            assert False, f'Unsupported Operation {oper}'
    
    cache[key] = results['z']
    return results['z']


def evaluate_model_number(model_num: int, rules: defaultdict):

    model_num_str = str(model_num)

    z_input = 0
    cache = {}
    for index, m_digit in enumerate(model_num_str):
        z_input = apply_rule(int(m_digit), z_input, index, rules, cache)

    return z_input


def test1():
    
    start = 99999999999999

    found = False
    while not found:
        m = str(start)


        if m.count('0') == 0:
            result = calculate(m)
            if result['z'] == 0:
                print(f'Model {m} is valid. {result=}')
            else:
                # print(f'Model {m} is NOT valid. {result=}')
                pass
            # print(f'{m=} {result=}')
        start -= 1

        if start < 10000000000000:
            assert False, f'Failed to find a model number'

#test1()



def test2():

    rules = load_rules()
    start = 99999999999999

    found = False
    while not found:
        m = str(start)
        #print(f'Processing Model {m}')
        if m.count('0') == 0: # No Zeros in the number
            result = evaluate_model_number(m, rules)
            if result == 0:
                print(f'Model {m} is valid. {result=}')
            else:
                # print(f'Model {m} is NOT valid. {result=}')
                pass
            # print(f'{m=} {result=}')
        start -= 1

        if start < 10000000000000 or start < 99999989998888:
            assert False, f'Failed to find a model number'

#test1()

test2()