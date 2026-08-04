# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l,r = [], []
        def dfs(tree, l) -> None:
            if not tree: 
                l.append(None) 
                return
            l += [tree.val]
            dfs(tree.left, l)
            dfs(tree.right, l)
        dfs(p, l)
        dfs(q, r)
        return l == r