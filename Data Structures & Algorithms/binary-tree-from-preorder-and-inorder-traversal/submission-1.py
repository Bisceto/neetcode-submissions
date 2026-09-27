# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hm = {val: idx for idx, val in enumerate(inorder)}
        self.root_idx = 0

        def buildSubtree(in_l, in_r):
            if in_l > in_r:
                return None
            # Root is the first element of preorder
            root_val = preorder[self.root_idx]
            node = TreeNode(root_val)
            mid = inorder_hm[root_val]
            self.root_idx += 1
            # Find the corresponding root in inorder. Find left and right subtree
            # Key intuition: I always consume preorder left to right. Is only the inorder subarrays that i need to track

            node.left = buildSubtree(in_l, mid - 1)            
            node.right = buildSubtree(mid + 1, in_r)            
            return node


        
        return buildSubtree(0, len(inorder) - 1)
