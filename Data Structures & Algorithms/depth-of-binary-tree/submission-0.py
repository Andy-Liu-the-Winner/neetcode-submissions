# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        m = 0
        def dfs(t, l):
            nonlocal m
            if not t:
                m = max(m, l)
                return l
            dfs(t.left, l + 1)
            dfs(t.right, l + 1)
        dfs(root, 0)
        return m
