# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        d = {0:[]}
        def dfs(tree, level):
            if not tree: return
            if level in d:
                d[level].append(tree.val)
            else:
                d[level] = [tree.val]
            dfs(tree.left, level + 1)
            dfs(tree.right, level + 1)
        dfs(root, 0)
        # construct list from dict 
        l = len(d)
        res = [[] for i in range(l)]
        for k, v in d.items():
            res[k] = v
        return res
        