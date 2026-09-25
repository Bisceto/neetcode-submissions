# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        st = [(root, 1)]
        while st:
            cur, lvl = st.pop()
            res = max(res, lvl)
            if cur.left:
                st.append((cur.left, lvl + 1))
            if cur.right:
                st.append((cur.right, lvl + 1))
        return res