# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        root.val = 0
        while q:
            level_sum = 0
            for node in q:
                if node.left:
                    level_sum += node.left.val
                if node.right:
                    level_sum += node.right.val
            for i in range(len(q)):
                sib_sum = 0
                node = q.popleft()
                
                if node.left:
                    sib_sum += node.left.val
                if node.right:
                    sib_sum += node.right.val

                if node.left:
                    node.left.val = level_sum - sib_sum
                    q.append(node.left)
                if node.right:
                    node.right.val = level_sum - sib_sum
                    q.append(node.right)
        return root
