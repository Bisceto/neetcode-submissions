# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(list)
        dq = deque([(root, 0)])
        while dq:
            cur, lvl = dq.popleft()
            if not cur:
                continue
            res[lvl].append(cur.val)
            dq.append((cur.left, lvl + 1))
            dq.append((cur.right, lvl + 1))

        return list(res.values())