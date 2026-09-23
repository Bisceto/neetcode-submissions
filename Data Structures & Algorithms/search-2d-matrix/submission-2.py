class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lm, ln = 0, 0
        rm, rn = m - 1, n - 1 
        while lm <= rm and ln <= rn:
            midm = (lm + rm) // 2 % m
            midn = (ln + rn) // 2 % n
            val = matrix[midm][midn]
            if val == target:
                return True
            elif val > target:
                if rn == 0:
                    rm -= 1
                    rn = n - 1
                else:
                    rn -= 1
            else: #shift left pointer up
                if ln == n - 1:
                    lm += 1
                    ln = 0
                else:
                    ln += 1
        return False