# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(tree):
            if not tree: return 
            tmp = tree.left
            tree.left = tree.right
            tree.right = tmp
            invert(tree.left)
            invert(tree.right)
        invert(root)
        return root
