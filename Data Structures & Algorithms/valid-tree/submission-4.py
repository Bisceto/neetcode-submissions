class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # What makes a valid tree? 
        # No cycles. How to determine no cycles in an undirected graph? keep track of the node's parent and we revisit that parent it is okay. else is cycle
        # Important edge case: n node must have n-1 edges in a tree
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # 0 is unexplored, [1] is exploring, [2] is explored
        state = [0] * n
        # Keep track of the (parent, cur)
        def dfs(parent, cur):
            if state[cur] == 2:
                return True
            elif state[cur] == 1:
                return False
            else: # Not explored
                state[cur] = 1
                for nei in graph[cur]:
                    if nei == parent:
                        continue
                    elif not dfs(cur, nei):
                        return False
                state[cur] = 2
                return True

        for key in range(n):
            if not dfs(None, key): #Treat every node as the root
                return False

        return True
            
