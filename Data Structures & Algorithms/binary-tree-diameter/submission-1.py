# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive method
        # if not root:
        #     return 0
        # self.max_diameter = 0
        # def height(node):
        #     if not node:
        #         return 0
        #     left_height = height(node.left)
        #     right_height = height(node.right)
        #     self.max_diameter = max(self.max_diameter, left_height + right_height)
        #     return 1 + max(left_height, right_height)
        # height(root)

        # return self.max_diameter
        
        # Iterative method. Visited means we have the max height for that node
        st = [(root, False)]
        hm = defaultdict(int)
        max_diameter = 0
        while st:
            cur, visited = st.pop()
            if cur is None:
                continue
            if not visited:
                st.append((cur, True))
                st.append((cur.left, False))
                st.append((cur.right, False))
            else:
                max_diameter = max(max_diameter, hm[cur.left] + hm[cur.right])
                hm[cur] = 1 + max(hm[cur.left], hm[cur.right])

        return max_diameter








