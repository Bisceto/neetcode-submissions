class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited = [False] * n
        res = 0
        def dfs(x):
            st = [x]
            while st:
                cur = st.pop()
                if visited[cur]:
                    continue
                visited[cur] = True
                for nei in adjList[cur]:
                    st.append(nei)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1
        
        return res
