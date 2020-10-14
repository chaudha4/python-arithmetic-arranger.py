# Iterate over two lists

alist = ["Red", "Blue", "Green"]
blist = [22, 33, 44]
for ii, jj in zip(alist, blist):
    print(f"There are {jj} {ii} balls.")


# Update the counts
for idx, val in enumerate(alist):
    if  val == "Blue":
        blist[idx] *= 100

for ii, jj in zip(alist, blist):
    print(f"There are {jj} {ii} balls.")