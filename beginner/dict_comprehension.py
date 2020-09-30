
dict1 = {ii:ii for ii in range(1,5)}
print(dict1)    #{1: 1, 2: 2, 3: 3, 4: 4}


dict1 = {ii:vv for ii,vv in enumerate(range(11, 15))}
print(dict1)    #{0: 11, 1: 12, 2: 13, 3: 14}

dict1 = {str(ii):float(vv) for ii,vv in enumerate(range(11, 15))}
print(dict1)    #{'0': 11.0, '1': 12.0, '2': 13.0, '3': 14.0}

# example of zip
keys = ['a','b','c','d','e'] 
values = [1,2,3,4,5]  
myDict = { k:v for (k,v) in zip(keys, values)}   
print(myDict)   #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}



fx = lambda k,v: {k,v}
print(fx("a",10))