# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isMatchingTree(node, subnode):
            if node is None and subnode is None:
                return True
            st = [(node, subnode)]
            while st:
                node, subnode = st.pop()
                if not node and not subnode:
                    continue
                if not node or not subnode or node.val != subnode.val:
                    return False
                st.append((node.left, subnode.left))
                st.append((node.right, subnode.right))
            return True
        
        st = [root]
        while st:
            cur = st.pop()
            if not cur:
                continue
            if isMatchingTree(cur, subRoot):
                return True
            else:
                st.append(cur.left)
                st.append(cur.right)
        return False
                