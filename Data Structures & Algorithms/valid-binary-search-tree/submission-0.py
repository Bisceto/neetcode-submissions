# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # In order traversal, pure acsending
        st = []
        cur = root
        prev = float('-inf')
        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.left
            cur = st.pop() #leftmose visited node
            if cur.val > prev:
                prev = cur.val
            else:
                return False
            cur = cur.right
        return True