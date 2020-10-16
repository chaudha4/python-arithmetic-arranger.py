import random
import logging

logging.basicConfig(level=logging.CRITICAL, format='%(process)d-%(levelname)s-%(message)s')


WINNING_MOVE = {"R": "P", "P": "S", "S": "R"}


def count_substr(s, ss):
    count = 0
    for idx, _ in enumerate(s):
        if s[idx:idx+len(ss)] == ss:
            count += 1
    return count


def look_for_pattern(opponent_history):

    oh_len = len(opponent_history)
    pat_size = 4  # Start looking from here and go up.
    count_list = []  # Store the count of patterns seen
    pattern_list = []

    in_str = "".join(opponent_history)

    while (pat_size < oh_len):
        count_list.append(count_substr(in_str, in_str[-pat_size:]))
        pattern_list.append(in_str[-pat_size:])
        pat_size += 1

    max_seen = 0
    max_idx = 0
    idx = 0
    for vl in count_list:
        if (vl > max_seen):
            max_seen = vl
            max_idx = idx
        idx += 1

    # Now that we know the most frequest pattern played, lets find the most likely next move.
    next_move_R_cnt = count_substr(in_str, pattern_list[max_idx] + "R")
    next_move_P_cnt = count_substr(in_str, pattern_list[max_idx] + "P")
    next_move_S_cnt = count_substr(in_str, pattern_list[max_idx] + "S")

    cutoff = 2 * (oh_len/100)  # 20% or less means really no pattern found.

    next_move = ""
    if next_move_R_cnt > cutoff or next_move_P_cnt > cutoff or next_move_S_cnt > cutoff:
        if (next_move_R_cnt > next_move_S_cnt):
            if (next_move_R_cnt > next_move_P_cnt):
                next_move = "R"
            else:
                next_move = "P"
        else:
            if (next_move_S_cnt > next_move_P_cnt):
                next_move = "S"
            else:
                next_move = "P"

    logging.info(f"Pattern Seen R{next_move_R_cnt} P{next_move_P_cnt} S{next_move_S_cnt} Predict[{next_move}].")
    return next_move

def play_least_used_set(history, threshold=.20):
    lm = history[-1]    # Last Move
    pm = [lm + xx for xx in ['R', 'P', 'S']]    # possible Moves
    cpm = [0,0,0]   # possible Moves Counts

    # Find which of the possible moves is least frequently played.
    in_str = "".join(history)
    for ii, vv in enumerate(pm):
        cpm[ii] = count_substr(in_str, vv)

    least = maxc = cpm[0]
    lmov = mmov = pm[0]
    for ii, jj in zip(pm, cpm):
        if jj < least:
            least = jj
            lmov = ii
        if jj > maxc:
            maxc = jj
            mmov = ii

    spread = (maxc - least)/len(history)
    #logging.info(spread)
    #logging.info(pm)
    #logging.info(lmov[-1])

    if spread > threshold:
        return lmov[-1]

    return ""

def dont_copy_my_moves(myhistory, opphistory):
    match = True
    for xx, yy in zip(myhistory, opphistory[1:]):
        if (WINNING_MOVE[xx] != yy):
            match = False
            #break
    
    if match:
        # Opponent will play to win aginst my last move
        return WINNING_MOVE[myhistory[-1]]

    return ""

def player(prev_play, opponent_history=[], my_history=[]):

    random_play = random.choice(['R', 'P', 'S'])

    if prev_play == "":
        # First Play. Reset My Data.
        my_history.clear()
        opponent_history.clear()

    def done(my_play, guess="Random"):
        logging.info(f"My play {my_play}. Strategy {guess}.\n")
        my_history.append(my_play)
        return my_play

    def didIlose(me, other):
        if (me == other):
            return True     # Tie
        if (WINNING_MOVE[me] == other):
            return True     # Opponent won
        return False         # I won

    if not prev_play == "":
        opponent_history.append(prev_play)

    # Play random Initially
    if len(opponent_history) < 5:
        return done(random_play)

    """
    if didIlose(my_history[-1], opponent_history[-1]) and didIlose(my_history[-2], opponent_history[-2]):
        # Haven't won in last two games. Lets play random.
        logging.info(f"Lost Twice already. Lets copy opponent move")
        return done(random_play)
    """

    # Look a my last few moves and see if opponent used it to make their next move
    opp_move = dont_copy_my_moves(my_history[-10:], opponent_history[-10:])
    if (opp_move != ""):
        return done(WINNING_MOVE[opp_move], "I know You will play to my last move")    

    # Is my opponent using a frequent pattern in my moves. 
    opp_move = play_least_used_set(my_history)
    if (opp_move != ""):
        return done(opp_move, "Play Least Used Set with Default Threshold")    

    # Lets now look for a pttern in opponents move
    opp_move = look_for_pattern(opponent_history)
    if (opp_move != ""):
        return done(WINNING_MOVE[opp_move], "Use Opponent Play Pattern")

    # Is my opponent using a less frequent pattern in my moves. 
    opp_move = play_least_used_set(my_history, .005)
    if (opp_move != ""):
        return done(opp_move, "Play Least Used Set with .005 Threshold")    



    """

    ii = 5
    if (len(opponent_history) > ii):
        opp_copying_my_moves = True
        logging.info(f"{o_h[-ii:]}, {my_history[-ii:]}")
        for me, opnt in zip(o_h[-ii:], my_history[-ii:]):
            logging.info(
                f"Check History - My Move: {WINNING_MOVE[me]}, Opponent Move: {opnt}")
            if WINNING_MOVE[me] != opnt:
                opp_copying_my_moves = False

    # my_history.append(random_play)
    """
    return done(random_play)

"""
player("P", ["S", "R", "P", "S", "S", "R", "R", "P", "R", "S", "R"], [
       "S", "R", "P", "S", "S", "R", "S", "P", "R", "S", "P"])
"""
play_least_used_set(["S", "R", "P", "S", "S", "R", "R", "P", "R", "S", "P"])
