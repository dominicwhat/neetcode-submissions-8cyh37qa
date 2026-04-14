class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        fresh = 0
        result = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                if grid[i][j] == 1:
                    fresh += 1
        while q:
            for _ in range(len(q)):
                print(q)
                i, j, count = q.popleft()
                result = max(result, count)
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    if (x >= 0 and x < ROWS and y >= 0 and y < COLS and grid[x][y] == 1):
                        fresh -= 1
                        grid[x][y] = 2
                        q.append((x, y, count + 1))
        if fresh > 0:
            return -1
        else:
            return result
        