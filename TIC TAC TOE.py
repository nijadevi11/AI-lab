# Tic-Tac-Toe using MINIMAX

def display(board):
    for row in board:
        print(" ".join(row))


def check_winner(board):
    # Rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '_':
            return board[i][0]

    # Columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '_':
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return board[0][2]

    return None


def is_full(board):
    for row in board:
        if '_' in row:
            return False
    return True


# MINIMAX
def minimax(board, maximizing):

    winner = check_winner(board)

    if winner == 'O':
        return 1

    if winner == 'X':
        return -1

    if is_full(board):
        return 0

    if maximizing:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = '_'
                    best = max(best, score)

        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = '_'
                    best = min(best, score)

        return best


# Computer's best move
def computer_move(board):

    best_score = -1000
    best_move = None

    for i in range(3):
        for j in range(3):

            if board[i][j] == '_':
                board[i][j] = 'O'

                score = minimax(board, False)

                board[i][j] = '_'

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    board[best_move[0]][best_move[1]] = 'O'

    return best_move


# INPUT
print("Enter the Tic-Tac-Toe board")
print("Use X for Human, O for Computer and _ for empty")

board = []

for i in range(3):
    row = input("Enter row " + str(i + 1) + ": ").split()
    board.append(row)


print("\nInput Board:")
display(board)


# Computer makes move
move = computer_move(board)

print("\nComputer places O in position:",
      (move[0] + 1, move[1] + 1))


print("\nOutput Board:")
display(board)


# Check result
winner = check_winner(board)

if winner == 'O':
    print("Computer Wins")

elif winner == 'X':
    print("Human Player Wins")

elif is_full(board):
    print("Game Draw")

else:
    print("Game continues")
