
# https://adventofcode.com/2021/day/21#part2

# https://github.com/mebeim/aoc/blob/master/2021/README.md#day-21---dirac-dice


def play_game1(my_pos, my_score, my_win_count, his_pos, his_score, his_win_count):

    assert  0 < my_pos < 11, f'{my_pos=} must be 1-10'
   
    # if his_score > 20:
    #     his_win_count = his_win_count + 1
    #     return my_win_count, his_win_count

    for player_rolled1 in range(1,4):
        for player_rolled2 in range(1,4):
            for player_rolled3 in range(1,4):
                toMove = player_rolled1 + player_rolled2 + player_rolled3
                my_pos = my_pos + toMove
                if my_pos > 10:
                    my_pos = my_pos % 10

                if my_pos == 0:
                    # Handle the case where new_pos is 100 or 200 etc. In that case, it should land on 10 and not zero !!
                    my_pos = 10

                assert  0 < my_pos < 11, f'{my_pos=} {my_pos=} {toMove=}'

                my_score = my_score + my_pos

                # Did I win
                if my_score > 20:
                    my_win_count = my_win_count + 1
                    print(f'Game Over in this universe !! - {my_score=} {my_pos=} {his_score=} {his_pos=} {my_win_count=}')
                    return my_win_count, his_win_count                               

                # I did not win. The other player rolls the dice.
                his_win_count, my_win_count = play_game(his_pos, his_score, his_win_count, my_pos, my_score, my_win_count)

                
    return my_win_count, his_win_count
   
def play_game(my_pos, my_score, his_pos, his_score):

    assert  0 < my_pos < 11, f'{my_pos=} must be 1-10'

    if my_score > 20:
        return 1, 0
    
    if his_score > 20:
        return 0, 1
    
    my_win_count = his_win_count = 0

    for player_rolled1 in range(1,4):
        for player_rolled2 in range(1,4):
            for player_rolled3 in range(1,4):
                toMove = player_rolled1 + player_rolled2 + player_rolled3
                my_pos = my_pos + toMove
                if my_pos > 10:
                    my_pos = my_pos % 10

                if my_pos == 0:
                    # Handle the case where new_pos is 100 or 200 etc. In that case, it should land on 10 and not zero !!
                    my_pos = 10

                assert  0 < my_pos < 11, f'{my_pos=} {my_pos=} {toMove=}'

                my_score = my_score + my_pos                       

                his_count, my_count = play_game(his_pos, his_score, my_pos, my_score)

                my_win_count += my_count
                his_win_count += his_count



                
    return my_win_count, his_win_count
   


def solution1():
    my_win_count, his_win_count = play_game(1, 0, 5, 0,)
    print(f'{my_win_count=} {his_win_count=}')
    

#solution1()


# Anything below is NOT my solution :(

QUANTUM_ROLLS = []

for die1 in range(1, 4):
    for die2 in range(1, 4):
        for die3 in range(1, 4):
            QUANTUM_ROLLS.append(die1 + die2 + die3)

# This code copied from https://github.com/mebeim/aoc/blob/master/2021/README.md#day-21---dirac-dice
# Still cannot understand why my solution does not work.

# This will be very slow since it calculates the outcome again for the same input. 
# See play2 for memoization optimization technique to speed up

def play1(my_pos, my_score, other_pos, other_score):
    if my_score >= 21:
        return 1, 0

    if other_score >= 21:
        return 0, 1

    state = (my_pos, my_score, other_pos, other_score,)
  
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

    state = (my_pos, my_score, other_pos, other_score,)

    if state in cache:
        return cache[state]
    
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

    cache[state] = my_wins, other_wins
    return my_wins, other_wins


    
def testPlay2():
    wins = play2(4, 0, 8, 0)
    best = max(wins)
    print('Part 2:', best)

testPlay2()


