class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs / dfs. Idea is that we start at 0,0: when we find land. we do bfs and expand as far as we can
        res = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    q = deque([(i, j)])
                    while q:
                        i, j = q.popleft()
                        if i < 0 or i == m or j < 0 or j == n:
                            continue
                        if grid[i][j] == "0" or grid[i][j] == "#":
                            continue
                        else:
                            grid[i][j] = "#"

                            q.append((i + 1, j))
                            q.append((i - 1, j))
                            q.append((i, j + 1))
                            q.append((i, j - 1))
        
        return res
                        

