# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        res = []
        
        def dfs(t):
            if not t: return 
            dfs(t.left)
            res.append(t.val)
            dfs(t.right)
        dfs(root)
        return res