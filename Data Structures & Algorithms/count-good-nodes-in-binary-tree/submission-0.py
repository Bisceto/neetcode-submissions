# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0 
        st = [(root, float('-inf'))]
        while st:
            node, cur_max = st.pop()
            if node:
                if node.val >= cur_max:
                    res += 1
                st.append((node.left, max(node.val, cur_max)))
                st.append((node.right, max(node.val, cur_max)))
        return res
            