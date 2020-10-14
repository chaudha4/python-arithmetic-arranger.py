
# identify the max value in a list
alist = [1,2,3,4,4,4,4,5,6,6,7,7,1,2,3,4]
amax = max(alist)
print("Highest Value in the List is", amax)

# identify the unique entries
alist = [1,2,3,4,4,4,4,5,6,6,7,7,1,2,3,4]
print("Unique Values", set(alist))

# identify the max occurance of a value in a list
alist = [1,2,3,4,4,4,4,5,6,6,7,7,1,2,3,4]
amax = max(set(alist), key=alist.count)
print("The most frequent entry in the list is", amax)