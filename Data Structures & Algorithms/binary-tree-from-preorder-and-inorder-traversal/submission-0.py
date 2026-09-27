# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # elements to the right is the right subtree.
        # Do recursively? For left subtree and right subtree
        inorder_hm = defaultdict(int)
        for idx, val in enumerate(inorder):
            inorder_hm[val] = idx

        def buildSubtree(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r or in_l > in_r:
                return None
            # Root is the first element of preorder
            node = TreeNode(preorder[pre_l])
            # Find the corresponding root in inorder. Find left and right subtree
            inorder_idx = inorder_hm[preorder[pre_l]]
            inorder_left_end = inorder_idx - 1            
            inorder_right_start= inorder_idx + 1
            preorder_left_size = inorder_left_end - in_l + 1
            preorder_right_size = in_r - inorder_right_start + 1

            node.left = buildSubtree(pre_l + 1, pre_l + 1 + preorder_left_size - 1, in_l, inorder_left_end)            
            node.right = buildSubtree(pre_l + 1 + preorder_left_size, pre_l + 1 + preorder_left_size + preorder_right_size - 1, inorder_right_start, in_r)            
            return node


        
        return buildSubtree(0, len(preorder) - 1, 0, len(inorder) - 1)
