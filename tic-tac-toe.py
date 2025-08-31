def print_board(board):
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("--+---+--")

def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def board_full(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn:")

        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter values between 0 and 2.")
                continue
                
            if board[row][col] != " ":
                print("This spot is already taken! Try again.")
                continue
                
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
