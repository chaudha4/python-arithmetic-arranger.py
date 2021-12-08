


def age(state):

    new_fish = 0

    for ii, val in enumerate(state):
        if (val == 0):
            state[ii] = 6
            new_fish = new_fish + 1
        else:
            state[ii] = val - 1
    
    for ii in range(new_fish):
        state.append(8)
    
    return state


st = [2,1,1,1,1,1,1,5,1,1,1,1,5,1,1,3,5,1,1,3,1,1,3,1,4,4,4,5,1,1,1,3,1,3,1,1,2,2,1,1,1,5,1,1,1,5,2,5,1,1,2,1,3,3,5,1,1,4,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,4,1,5,1,2,1,1,1,1,5,1,1,1,1,1,5,1,1,1,4,5,1,1,3,4,1,1,1,3,5,1,1,1,2,1,1,4,1,4,1,2,1,1,2,1,5,1,1,1,5,1,2,2,1,1,1,5,1,2,3,1,1,1,5,3,2,1,1,3,1,1,3,1,3,1,1,1,5,1,1,1,1,1,1,1,3,1,1,1,1,3,1,1,4,1,1,3,2,1,2,1,1,2,2,1,2,1,1,1,4,1,2,4,1,1,4,4,1,1,1,1,1,4,1,1,1,2,1,1,2,1,5,1,1,1,1,1,5,1,3,1,1,2,3,4,4,1,1,1,3,2,4,4,1,1,3,5,1,1,1,1,4,1,1,1,1,1,5,3,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,5,1,4,4,1,1,1,1,1,1,1,1,3,1,3,1,4,1,1,2,2,2,1,1,2,1,1]
#print("Initial State:", st)
ii = 0
for ii in range(1, 81):
    st = age(st)
    #print("After ", ii, " day: ", st)

print("Total Fish after ", ii, " days: ", len(st))
