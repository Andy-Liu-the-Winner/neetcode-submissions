# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # root, left, right
        l = []
        def dfs(t):
            if not t:
                return 
            l.append(t.val)
            dfs(t.left)
            dfs(t.right)
        dfs(root)
        return l