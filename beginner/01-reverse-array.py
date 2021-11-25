
a = [1,2,3]
b = []
i = len(a)-1

while (i >= 0):
    print("Using While loop - ", a[i])
    b.append(a[i])
    i -= 1

print(b)

# Shortcut

c = a[::-1]
print(c)

#https://docs.python.org/3/tutorial/datastructures.html

for aa in reversed(a):
    print("Using reversed - ", aa)

b = list(reversed(a))
print(b)