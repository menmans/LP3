class NQBacktracking:
    def __init__(self, x_, y_):
        # Arrays to keep track of queen positions in diagonals and columns
        self.ld = [0] * 30  # Left diagonal
        self.rd = [0] * 30  # Right diagonal
        self.cl = [0] * 30  # Column array
        self.x = x_ - 1  # Convert 1-based index to 0-based for row
        self.y = y_ - 1  # Convert 1-based index to 0-based for column

    def printSolution(self, board):
        print("N Queen Backtracking Solution:\nGiven initial position of 1st queen at row:", self.x + 1,
              "column:", self.y + 1, "\n")
        for line in board:
            print(" ".join(map(str, line)))

    def solveNQUtil(self, board, col):
        N = len(board)
        # Base case: if all queens are placed
        if col >= N:
            return True

        # Skip the column where the first queen was initially placed
        if col == self.y:
            return self.solveNQUtil(board, col + 1)

        for i in range(N):
            # Skip the row where the first queen was initially placed
            if i == self.x:
                continue

            # Check if the queen can be placed at board[i][col]
            if (self.ld[i - col + N - 1] != 1 and
                    self.rd[i + col] != 1 and
                    self.cl[i] != 1):

                # Place queen and mark row, column, and diagonals as occupied
                board[i][col] = 1
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 1

                # Recursive call to place queen in next column
                if self.solveNQUtil(board, col + 1):
                    return True

                # BACKTRACK: remove queen and unmark row, column, and diagonals
                board[i][col] = 0
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 0

        return False

    def solveNQ(self):
        N = 4  # Board size (N x N)
        # Initialize board with all zeros
        board = [[0 for _ in range(N)] for _ in range(N)]
        # Place the first queen at the given position
        board[self.x][self.y] = 1
        # Mark the row, column, and diagonals for the first queen
        self.ld[self.x - self.y + N - 1] = self.rd[self.x + self.y] = self.cl[self.x] = 1

        # Start solving the problem
        if not self.solveNQUtil(board, 0):
            print("Solution does not exist")
            return False

        # Print the solution if one is found
        self.printSolution(board)
        return True

if __name__ == "__main__":
    N = 4  # Board size (N x N)
    x, y = 1, 3  # Initial position of the first queen (1-based indexing)
    NQBt = NQBacktracking(x, y)
    NQBt.solveNQ()
