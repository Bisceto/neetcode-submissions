# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        st = [(p, q)]
        while st:
            p, q = st.pop()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            st.append((p.left, q.left))
            st.append((p.right, q.right))
        return True