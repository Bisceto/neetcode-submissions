"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # Original : New node. Presence inside means visited and copied
        hm = {node: Node(node.val)}
        q = deque([node])
        while q:
            original = q.popleft()
            for nei in original.neighbors:
                if nei not in hm:
                    hm[nei] = Node(nei.val)
                    q.append(nei)
                hm[original].neighbors.append(hm[nei])

        return hm[node]