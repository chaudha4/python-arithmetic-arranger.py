
a = [1,2,3]
b = []
i = len(a)-1

while (i >= 0):
    print(a[i])
    b.append(a[i])
    i -= 1

print(b)

# Shortcut

c = a[::-1]
print(c)

