class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i, j):
            if(i >= 0 and i < ROWS and j >= 0 and j < COLS and board[i][j] == 'O'):
                board[i][j] = 'T'
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    dfs(x, y)
        for i in range(ROWS):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][COLS-1] == 'O':
                dfs(i, COLS-1)
        for j in range(COLS):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[ROWS-1][j] == 'O':
                dfs(ROWS-1, j)  
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'        


            