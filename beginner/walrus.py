import random


"""
Assignment expression are written with a new notation (:=).This operator is often called the walrus operator 
as it resembles the eyes and tusks of a walrus on its side.

Assignment expressions allow you to assign and return a value in the same expression. For example
"""

def walrus_demo(jj):
    
    if ( ii:= random.randint(1,100) ) > jj:
        print(f"Walrus operator := set ii to {ii} which is greater than {jj}")
    else:
        print(f"Walrus operator := set ii to {ii}")


walrus_demo(30)

