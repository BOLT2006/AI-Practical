N = 8

# Function to print the chessboard
def print_board(board):
    for row in board:
        for x in row:
            if x == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Function to check whether queen placement is safe
def is_safe(board, row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(
        range(row - 1, -1, -1),
        range(col - 1, -1, -1)
    ):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(
        range(row - 1, -1, -1),
        range(col + 1, N)
    ):
        if board[i][j] == 1:
            return False

    return True


# Function to solve using backtracking
def solve(board, row=1):

    # Base condition
    if row == N:
        print("Final 8-Queens Solution:")
        print_board(board)
        return True

    # Try every column
    for col in range(N):  # try every column in this row

        if is_safe(board, row, col):

            board[row][col] = 1   # place queen

            if solve(board, row + 1):  # place queen
                return True

            # Backtracking
            board[row][col] = 0  # didn't work → remove queen (backtrack)

    return False  # no column worked in this row


# Create empty chessboard
board = [[0] * N for _ in range(N)]

# Place first queen
board[0][0] = 1

print("Starting board:")
print_board(board)

# Start solving
if not solve(board):
    print("No solution found!")