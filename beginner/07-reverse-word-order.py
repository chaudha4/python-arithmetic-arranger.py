
"""
Reverse Word Order
"""

a = "My Name is Abhishek"
b = a.split()
c = ""

for bb in reversed(b):
    print(bb)
    c = c + bb + " "

print(c)