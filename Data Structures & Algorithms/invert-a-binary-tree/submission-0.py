# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        st = []
        st.append(root)
        while st:
            cur = st.pop()
            left = cur.left
            right = cur.right
            cur.left = right
            cur.right = left
            if cur.left:
                st.append(cur.left)
            if cur.right:
                st.append(cur.right)
        return root
            
