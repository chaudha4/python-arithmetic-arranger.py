"""
Take two lists, say for example these two:
	a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
"""


a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


#Using loop
c = []
for aa in a:
    for bb in b:
        if aa == bb:
            c.append(aa)

print("Using Loop - ", c)


# Using set
c = list(set(a) & set(b))
print("Using set() - ", c)

# Using list comprehensions 
c = [aa for aa in a for bb in b if aa==bb]
print("Using list comprehensions - ", c)