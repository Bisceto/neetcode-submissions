class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        INF = 2147483647
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                    # Multi Source BFS, add all the sources to the q first. so after every "treasure" is processed, we can guarantee that the first wave of points added is guaranteed to be the minimum

        while q:
            i, j = q.popleft()
            for d in DIRECTIONS:
                nr, nc = i + d[0], j + d[1]
                if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] != INF: 
                    continue
                grid[nr][nc] = grid[i][j] + 1
                q.append((nr, nc))



