
# Combine characters in an array to a string
alist = ["A", "B", "C"]
astr = "".join(alist)
print(astr)

# Use list comprehension to manipulate
bstr = "".join(cc + "-" for cc in alist)
print(bstr)

# Reverse the string
cstr = "".join(alist[-1::-1])
print(cstr)

# Put the string back to array
astr = "Abhishek"
alist = [xx for xx in astr]
print(alist)