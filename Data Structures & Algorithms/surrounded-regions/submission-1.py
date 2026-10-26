class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m)] # Actually dont need visited grid. we can change to a temporary 'T' before changing back to 'O'
        # Intuition: Look at the border cells and perform bfs/dfs on the 'O's. We keep a state for all visited that these are not
        # surrounded regions. 
        # Then we parse through the board again, for the 'O's that are not visited, we change to 'X'.
        st = []
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            if board[i][0] == 'O':
                st.append((i, 0))
            if board[i][n - 1] == 'O':
                st.append((i, n - 1))
        for j in range(n):
            if board[0][j] == 'O':
                st.append((0, j))
            if board[m - 1][j] == 'O':
                st.append((m - 1, j))
        
        while st:
            r, c = st.pop()
            if not visited[r][c]:
                visited[r][c] = 1
                for d in DIRECTIONS:
                    nr, nc = r + d[0], c + d[1]
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and board[nr][nc] == 'O':
                        st.append((nr, nc))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'



