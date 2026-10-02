class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_len = len(word)

        def backtrack(x, y, idx):
            if x == m or y == n or x < 0 or y < 0 or board[x][y] == '#':
                return False
            if board[x][y] == word[idx]:
                if idx == word_len - 1:
                    return True
                else: # Check all 4 directions for continuation
                    cur = board[x][y]
                    board[x][y] = '#'
                    res = backtrack(x + 1, y, idx + 1) or backtrack(x - 1, y, idx + 1) or backtrack(x, y + 1, idx + 1) or backtrack(x, y - 1, idx + 1)     
                    board[x][y] = cur
                    return res
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False