class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val != ".":
                    if val not in rows[i]:
                        rows[i].add(val)
                    else:
                        return False
                    if val not in cols[j]:
                        cols[j].add(val)
                    else:
                        return False
                    if val not in squares[(i // 3, j // 3)]:
                        squares[(i//3,j//3)].add(val)
                    else:
                        return False
        return True