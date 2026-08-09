# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_l, subroot_l = [], []
        def dfs(tree, l):
            if not tree: 
                l.append(None) 
                return
            l.append(tree.val)
            dfs(tree.left, l)
            dfs(tree.right, l)
        dfs(root, root_l)
        dfs(subRoot, subroot_l)
        for i in range(len(root_l) - len(subroot_l) + 1):
            if root_l[i: i + len(subroot_l)] == subroot_l: return True
        return False