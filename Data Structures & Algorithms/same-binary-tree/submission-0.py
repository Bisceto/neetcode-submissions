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
            if (p and not q) or (not p and q):
                return False
            if p.val == q.val:
                st.append((p.left, q.left))
                st.append((p.right, q.right))
            else:
                return False
        return True