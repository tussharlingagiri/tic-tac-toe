# 3x3 board
board = [[" " for _ in range(3)] for _ in range(3)]

def draw_board():
    #  board is a list of lists
    # i is counter and row is the value in the board
    for i, row in enumerate(board):
        # prints index value and row values
        print(f'Row {i}: {row}')
def get_move(player):
    # Run a loop and check various conditions to move the player either X or Y into an available position.
    # There is no pre-condition required before starting  this loop 
    # Hence use a "while True" infinite loop and break the infinite loop with return
    while True:
        # read user input into move
        move = input(f'{player}, enter your move (row column): ')  
        if len(move) != 2:
            print('Invalid move, try again')
            # continue the program and don't exit from the program if the condition not met
            continue  
        row, col = move
        if not row.isdigit() or not col.isdigit():
            print('isdigit validation encountered ... try again')
            continue
        # user might have entered row and column together as 11 or 12 or 21 etc.
        # so unpack those and assign to row and column
        row, col = int(row), int(col)

        if row < 0 or row > 2 or col < 0 or col > 2:
            print('row or col <0 or >2 encountered ... try again')
            continue
        if board[row][col] != ' ':
            print('That space is already occupied, try again')
            continue
        # break the begining infinite while loop
        return row, col
def check_winner():
    # check rows
    for row in board:
        print("inside check_winner, row value is : ", row)
        if row[0] != ' ' and row[0] == row[1] == row[2]:
            return row[0]
    # check columns
    for col in range(3):
        if board[0][col] != ' ' and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    # check diagonals
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    # return none because the winning condition is returned in above respective if methods
    return None
def main():
    draw_board()
    # run an infinite loop , to keep this program running
    while True:
        # game for two players each represented by X and Y. X for player1 and Y for player2.
        # The below loop runs each for X and Y. So each player gets a turn.
        for player in ['X', 'Y']:
            # occupy the position
            row, col = get_move(player)
            # assign player names to the above recorded position
            board[row][col] = player
            # draw the board marking the player
            draw_board()
            winner = check_winner()
            if winner:
                print(f'{winner},won')
                return
main()
