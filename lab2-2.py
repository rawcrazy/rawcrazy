EMPTY = " "
PLAYER_1 = "1"
PLAYER_2 = "2"

# Create Board
def create_board():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
# Show board
def show_board(board):
    for x in board:
        # Find better way to print this
        print("|".join(x))

# Place X on spot
def place_player(board, active_player, row, column):
    
    
    board[row-1][column-1] = active_player
    
# Check if someone has won
def check_if_win(board, active_player):
    
    # Making lists which will store the diagonals and columns of board
    diagonal1 = []
    diagonal2 = []
    column1 = []
    column2 = []
    column3 = []
    # Diagonal counter is used to index the different values in each row
    diagonal_counter = 1
    for row in board:
        # When each row is checked, the different indexes are organised
        # into the column and diagonal lists
        column1.append(row[0])
        column2.append(row[1])
        column3.append(row[2])
        diagonal1.append(row[diagonal_counter-1])
        diagonal2.append(row[-diagonal_counter])
        diagonal_counter += 1
        if "".join(row) == active_player * 3:
            return True
        
    # If statement which checks if any list is full of the active 
    # player's symbol
    if "".join(column1) == active_player * 3 or "".join(column2) == \
    active_player * 3 or "".join(column3) == active_player * 3:
        return True
    elif "".join(diagonal1) == active_player * 3 or "".join(diagonal2) \
    == active_player * 3:
        return True
    else:
        return False

def swap_player(active_player):
    if active_player == PLAYER_1:
        return PLAYER_2
    else:
        return PLAYER_1

def check(board,row,column):
    if board[row-1][column-1]==EMPTY:
       return 1;
    else:
        return 0;

def main():
    # Creates board and assigns starting player
    board = create_board()
    active_player = PLAYER_1
    i=0;
    flag1=0;
    while i<9:
        flag=True
        while flag:
            show_board(board)
        # Ask for player input
            row = int(input("\nIt is PLAYER {}'s turn play. Choose a row (1-3): \
              ".format(active_player)))
            column = int(input("Choose a column: "))
            if(check(board,row,column)):
                place_player(board, active_player, row, column)
                flag=False
        # Checks if player has won
        if check_if_win(board, active_player) is True:
            show_board(board)
            print("\n PLAYER {} IS WINNER!:Congratulations".format(active_player))
            flag1=1
            break
        active_player = swap_player(active_player)
        i=i+1;

    
    if(flag1==0):
        show_board(board)
        print("\n Match Draw!");
        
if __name__ == "__main__":
    main()
