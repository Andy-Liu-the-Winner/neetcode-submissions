# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(tree, s):
            if not tree: 
                s.append(None)
                return
            s.append(tree.val)
            dfs(tree.left, s)
            dfs(tree.right, s)
        s1, s2 = [], []
        dfs(root, s1)
        dfs(subRoot, s2)
        print(s1, s2)

        l1, l2 = len(s1), len(s2)
        if l2 > l1: return False
        for i in range(0, l1 - l2 + 1):
            if s1[i: i + l2] == s2:
                return True
        return False