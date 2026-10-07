class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        mins = 0
        q = deque()
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        if fresh == 0:
            return 0

        # fresh > 0 avoids the last round when all the fruits are already rotten
        while q and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()

                for d in DIRECTIONS:
                    nr, nc = i + d[0], j + d[1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] != 1: # Ensure we are capturing fresh neighbouring fruit once
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            mins += 1

        return mins if fresh == 0 else -1