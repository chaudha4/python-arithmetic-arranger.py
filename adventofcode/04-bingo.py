class board:

    def __init__(self, rows=5, cols=5) -> None:
        self.numbers = []
        self.called = []
        self.rows = rows
        self.cols = cols

    # add a row.
    def add(self, A):
        # Convert to int array
        data = [int(n) for n in A.split()]
        self.numbers.append(data)

        # Keep track of called numbers
        called = [False for _ in A.split()]
        self.called.append(called)
    
    # A new number is drawn. Mark it as called.
    def call(self, N):
        for ridx, row in enumerate(self.numbers):
            for cidx, col in enumerate(row):
                if (self.numbers[ridx][cidx] == N):
                    self.called[ridx][cidx] = True

    # Check if I won - All numbers in the col are called.
    def column_check(self):
        ret = True
        for ii in range(self.cols):
            ret = True
            for jj in range(self.rows):
                # Check Rows
                if (self.called[jj][ii] == False):
                    ret = False

            # Found a col with all numbers called. Stop
            if (ret):
                return ret
        return ret

    # Check if I won - All numbers in a row are called.
    def row_check(self):
        ret = True
        for ii in range(self.cols):
            ret = True
            for jj in range(self.rows):
                # Check Rows
                if (self.called[ii][jj] == False):
                    ret = False

            # Found a row with all numbers called. Stop
            if (ret):
                return ret
        return ret

    # return sum of all unmarked numbers on the board
    def get_sum(self):
        ret = 0
        for ii in range(self.cols):
            for jj in range(self.rows):
                if (self.called[ii][jj] == False):
                    ret = ret + self.numbers[ii][jj]

        return ret


    # Print called numbers in bold face.
    def __repr__(self) -> str:

        ret = ""
        for ridx, row in enumerate(self.numbers):
            for cidx, col in enumerate(row):
                pstr = ""
                if (self.called[ridx][cidx] == False):
                    pstr = str(col)
                else:
                    # Numbers that gave been called print in bold face
                    pstr = '\033[1m' + str(col) + '\033[0m'

                ret = ret + pstr + " "
            ret = ret + "\n"
        ret = ret + "\n"
        return ret



# Play the game
def play(cn, bl, wl):
    for nn in cn:
        print("Number called: ", nn)
        for index, b in enumerate(bl):
            num = int(nn)

            #skip if already won.
            if (wl[index] == True):
                continue

            b.call(num)
            if (b.column_check() == True):
                wl[index] = True
                result(b, num)
            if (b.row_check() == True):
                wl[index] = True
                result(b, num)


def result(board, N):
    print("-------Results------")
    print("Last number called is: ", N)
    print("Score                : ", board.get_sum() * N)
    print(board)




# Board List
bl = []

# Won list - Start with all False and set to True as you win.
wl = []

# Called Numbers
cn = []

with open("adventofcode/04-bingo.txt", "r") as f:
    data = f.read().split("\n")
    
    # Only first row is the called number. Save it.
    cn = data[0].split(",")

    # Rest all is board data (5X5). Process it.
    ii = 1
    while (ii < len(data)):
        if (data[ii] == ""):
            #print("Creating a new Board")
            bl.append(board())
            wl.append(False)
        else:
            #print("Adding to the board")
            bl[-1].add(data[ii])

        ii = ii + 1


play(cn, bl, wl)
