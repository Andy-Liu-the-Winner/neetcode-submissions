# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
  
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree, low, high):
            if not tree: return True

            if not (low < tree.val < high):
                return False
            else:
                return dfs(tree.left, low, tree.val) and dfs(tree.right, tree.val, high)

        return dfs(root, -999999999, 999999999)

