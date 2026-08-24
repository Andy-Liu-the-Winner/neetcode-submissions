# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return
        # build {node.val : [anc (tree obj)]}
        d = {}
        def bfs(tree):
            queue = [(tree, [])]
            while queue:
                curr, ancestors = queue.pop()
                current_path = ancestors + [curr]
                d[curr.val] = current_path
                if curr.left: queue.append((curr.left, current_path))
                if curr.right: queue.append((curr.right, current_path))
        bfs(root)

        p_path = d[p.val]
        q_path = d[q.val]
        lca = None
        for p_anc, q_anc in zip(p_path, q_path):
            if p_anc is q_anc:
                lca = p_anc
            else:
                break
        return lca




