class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Reverse BFS/DFS. We start from all the border cells and do BFS on the condition that neighbouring cells must be >= than current.
        # Store these valid cells in the pacific / atlantic sets. Then we do a intersection of sets to get the res.
        # Pacific set: i is 0, then j is all values, else only when j is 0
        # Atlantic Set: if i is m, then j is all values, else only when j is n 
        
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        st = []

        for i in range(m):
            st.append((pacific, i, 0))
            st.append((atlantic, i, n - 1)) 
        for j in range(n):
            st.append((pacific, 0, j))
            st.append((atlantic, m - 1, j)) 

        while st:
            s, i, j = st.pop()
            s.add((i, j))
            for d in DIRECTIONS:
                ni, nj = i + d[0], j + d[1]
                if ni < 0 or ni == m or nj < 0 or nj == n or heights[ni][nj] < heights[i][j] or (ni, nj) in s:
                    continue
                st.append((s, ni, nj))

        return list(pacific & atlantic)

