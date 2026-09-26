# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Post order traversal
        # Recursive method
        # if not root:
        #     return True

        # def height(node):
        #     if not node:
        #         return 0
        #     left_height = height(node.left)
        #     right_height = height(node.right)
        #     if left_height == -1 or right_height == -1:
        #         return -1
        #     elif abs(left_height - right_height) > 1:
        #         return -1
        #     return max(left_height, right_height) + 1

        # return height(root) >= 0

        # Iterative method
        if not root:
            return True
        hm = defaultdict(int)
        st = [(root, False)]
        while st:
            cur, visited = st.pop()
            if not cur:
                continue
            if not visited:
                st.append((cur, True))
                st.append((cur.left, False))
                st.append((cur.right, False))
            else:
                left_height = hm[cur.left]
                right_height = hm[cur.right]
                if abs(left_height - right_height) > 1:
                    return False
                hm[cur] = 1 + max(left_height, right_height)
        return True








