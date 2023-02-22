
# https://adventofcode.com/2021/day/21#part2

# This funtion needs caching. Will take too much time without it.
# memoization optimization technique to speed up example !!

def play_game(my_pos, my_score, his_pos, his_score, cache={}):

    assert  0 < my_pos < 11, f'{my_pos=} must be 1-10'

    # You might think that this will get set to zero on every regression call. And that is 
    # true but that is a different copy of it. This is a local variable. And we are only
    # interested in the outside/first one.
    my_win_count = his_win_count = 0

    # A closer look will reveal that the following code is never executed. So commented out.
    # Actually not required since his_score is the one that is actually updated
    # and passed in in the recursive calls.
    # if my_score >= 21:
    #     return 1, 0
    
    if his_score >= 21:
        return 0, 1
    
    # Save the input as a kay to cache. If we already did this calculation, no need to do it again. Use cache.
    key = (my_pos, my_score, his_pos, his_score,)
    if key in cache:
        return cache[key]
    
    for player_rolled1 in range(1,4):
        for player_rolled2 in range(1,4):
            for player_rolled3 in range(1,4):
                
                toMove = player_rolled1 + player_rolled2 + player_rolled3
                # Don't try to reuse my_pos by doing this below. Remember my_pos is reused for next iteration and 
                # you don't want to corrupt it. I wasted a lot of time with this following commented code !!
                # my_pos = my_pos + toMove
                my_new_pos = my_pos + toMove

                if my_new_pos > 10:
                    my_new_pos = my_new_pos % 10

                if my_new_pos == 0:
                    # Handle the case where new_pos is 100 or 200 etc. In that case, it should land on 10 and not zero !!
                    my_new_pos = 10

                assert  0 < my_new_pos < 11, f'{my_new_pos=} {my_pos=} {toMove=}'

                my_new_score = my_score + my_new_pos                       

                hc, mc = play_game(his_pos, his_score, my_new_pos, my_new_score, cache)

                my_win_count += mc
                his_win_count += hc

    # Save the hard work in cache. Don't want to do it again..ever !!
    cache[key] = my_win_count, his_win_count

    return my_win_count, his_win_count, 
   

def test_play_game():
    wins = play_game(4, 0, 8, 0)
    best = max(wins)
    assert best == 444356092776315
    print(f'{wins=} {best=} ')


def solution1():
    wins = play_game(1, 0, 5, 0)
    best = max(wins)
    assert best == 138508043837521
    print(f'{wins=} {best=}')
    

test_play_game()
solution1()


# Anything below is NOT my solution :(   
# I did fix some critical bugs though :)

# This code (I fixed a few bugs in it) copied from https://github.com/mebeim/aoc/blob/master/2021/README.md#day-21---dirac-dice

QUANTUM_ROLLS = []

for die1 in range(1, 4):
    for die2 in range(1, 4):
        for die3 in range(1, 4):
            QUANTUM_ROLLS.append(die1 + die2 + die3)




# This will be very slow since it calculates the outcome again for the same input. 
# See play2 for memoization optimization technique to speed up

def play1(my_pos, my_score, other_pos, other_score):
    if my_score >= 21:
        return 1, 0

    if other_score >= 21:
        return 0, 1
 
    my_wins = other_wins = 0

    for roll in QUANTUM_ROLLS:
        # Play one turn calculating the new score with the current roll:
        new_pos   = (my_pos + roll) % 10
        new_score = my_score + new_pos + 1

        # Let the other player play, swapping the arguments:
        ow, mw = play2(other_pos, other_score, new_pos, new_score)

        # Update total wins of each player:
        my_wins    += mw
        other_wins += ow

    return my_wins, other_wins


def play2(my_pos, my_score, other_pos, other_score, cache = {}):
    if my_score >= 21:
        return 1, 0

    if other_score >= 21:
        return 0, 1

    # Save the input as a kay to cache. If we already did this calculation, no need to do it again. Use cache.
    state = (my_pos, my_score, other_pos, other_score,)
    if state in cache:
        return cache[state]

    # Not in cache. Lets do the hard work now.    
    my_wins = other_wins = 0

    for roll in QUANTUM_ROLLS:
        # Play one turn calculating the new score with the current roll:
        new_pos   = (my_pos + roll) % 10

        if new_pos == 0:
            # Handle the case where new_pos is 100 or 200 etc. In that case, it should land on 10 and not zero !!
            new_pos = 10

        assert  0 < new_pos < 11, f'{new_pos=} {my_pos=}'

        new_score = my_score + new_pos

        # Let the other player play, swapping the arguments:
        ow, mw = play2(other_pos, other_score, new_pos, new_score)

        # Update total wins of each player:
        my_wins    += mw
        other_wins += ow

    # Save the hard work in cache. Don't want to do it again..ever !!
    cache[state] = my_wins, other_wins

    return my_wins, other_wins


    
def testPlay2():
    # wins = play2(4, 0, 8, 0)
    # best = max(wins)
    # print('Part 2 Example:', best)

    wins = play2(1, 0, 5, 0)
    print(wins)
    best = max(wins)
    print('Part 2 Question:', best)


#testPlay2()


