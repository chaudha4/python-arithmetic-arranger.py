
# https://adventofcode.com/2021/day/21


def play_game(start_postion, current_score, dice_num_rolled):

    assert  0 < start_postion < 11, f'{start_postion=} must be 1-10'

    rolled = [dice_num_rolled]

    for _ in range(2):
        dice_num_rolled = dice_num_rolled + 1
        if dice_num_rolled > 100:
            dice_num_rolled = 1
        rolled.append(dice_num_rolled)
    
    toMove = sum(rolled)

    new_pos = start_postion + toMove
    if new_pos > 10:
        new_pos = new_pos % 10
    
    if new_pos == 0:
        # Handle the case where new_pos is 100 or 200 etc. In that case, it should land on 10 and not zero !!
        new_pos = 10
    
    #assert  0 < new_pos < 11, f'{new_pos=} {start_postion=} {toMove=} {rolled=}'

    new_score = current_score + new_pos

    next_dice_num =  rolled[-1] + 1
    if next_dice_num > 100:
        next_dice_num = 1

    #print(f'{rolled=} {toMove=} {new_pos=} {new_score=}')

    #return new_pos, rolled[-1] + 1, new_score
    return new_pos, new_score, next_dice_num, rolled


def play(pos1, pos2):
    
    # player1
    score1 = 0
    
    # player2
    score2 = 0

    dice_value = 1
    rolled_count = 0
    player1_won = False
    final_score = None

    max_score = 0
    while max_score < 1000:
        # player1
        pos1, score1, dice_value, diceList = play_game(pos1, score1, dice_value)
        # print(f'Player 1 rolls {diceList} and moves to space {pos1} for a total score of {score1}.')
        rolled_count = rolled_count + 3

        if score1 > max_score:
            max_score = score1

        if max_score >= 1000:
            # If player 1 won, no need to go to player 2.
            player1_won = True
            break

        # player2
        pos2, score2, dice_value, diceList = play_game(pos2, score2, dice_value)
        # print(f'Player 2 rolls {diceList} and moves to space {pos2} for a total score of {score2}.')
        rolled_count = rolled_count + 3

        if score2 > max_score:
            max_score = score2

    if player1_won:
        final_score = rolled_count * score2
    else:
        final_score = rolled_count * score1       
    
    # print(f'{score1=} {score2=} {rolled_count=} {final_score=}')

    return final_score

def solution1():
    score = play(1, 5)
    print(f'Calculated {score=}. Expected score=432450.')
    

def test1():
    score = play(4,8)
    print(f'Calculated {score=}. Expected score=739785.')
    assert score == 739785
    

#test1()    
solution1()






    



