class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur = 0
                    st = [(i, j)]
                    while st:
                        i, j = st.pop()
                        if i < 0 or i == m or j < 0 or j == n or grid[i][j] != 1:
                            continue
                        cur += 1
                        grid[i][j] = 0
                        for direction in directions:
                            nr, nc = i + direction[0], j + direction[1]
                            st.append((nr, nc))
                    res = max(res, cur)
        return res

