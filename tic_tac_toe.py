def print_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def check_win(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    for i in range(0, 3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    return False

def play_game():
    board = [" "] * 9
    players = ["X", "O"]
    current_player = players[0]
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        move = int(input("Enter a position (1-9): ")) - 1
        if board[move] != " ":
            print("That position is already taken!")
            continue
        board[move] = current_player
        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if " " not in board:
            print_board(board)
            print("Tie game!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]

play_game()
