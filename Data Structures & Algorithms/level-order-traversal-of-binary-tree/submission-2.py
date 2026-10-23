# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([[root, 1]])
        while q:
            e, l = q.popleft()
            if len(res) < l:
                res.append([e.val])
            else:
                res[l - 1].append(e.val)
            if e.left:
                q.append([e.left, l + 1])
            if e.right:
                q.append([e.right, l + 1])
        return res