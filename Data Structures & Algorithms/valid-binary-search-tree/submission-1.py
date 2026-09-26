# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # In order traversal, pure ascending
        # st = []
        # cur = root
        # prev = float('-inf')
        # while cur or st:
        #     while cur:
        #         st.append(cur)
        #         cur = cur.left
        #     cur = st.pop() #leftmose visited node
        #     if cur.val > prev:
        #         prev = cur.val
        #     else:
        #         return False
        #     cur = cur.right
        # return 
        def valid(node, left, right):
            if not node:
                return True
            elif left < node.val and node.val < right:
                return valid(node.left, left, node.val) and valid(node.right, node.val, right)
            return False
        return valid(root, float('-inf'), float('inf'))
        
