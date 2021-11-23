a = [1,2,3]
b = [2,3,4,5,6]
c = []

for aa in a:
    found = True
    for bb in b:
        if (aa == bb):
            found = False
            break
    if (found):
        c.append(aa)


for aa in b:
    found = True
    for bb in a:
        if (aa == bb):
            found = False
            break
    if (found):
        c.append(aa)

print(c)


# shortcut
print(set(a) ^ set(b))