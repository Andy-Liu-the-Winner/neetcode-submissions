# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def check(e, level, left_val):
            if level % 2 == 0:
                if not e.val % 2 == 1:
                    return 123456789, False
                if not left_val == -9999999:
                    if left_val >= e.val:
                        return 123456789 ,False
            else:
                if not e.val % 2 == 0:
                    return 123456789, False 
                if not left_val == -9999999:
                    if left_val <= e.val:
                        return 123456789 ,False
            return e.val, True

        q = deque([(root, 0)])
        prev = {}

        def bfs():
            while q:
                e, level = q.popleft()

                left_val = prev.get(level, -9999999)
                new_left_val, check_bool = check(e, level, left_val)

                if not check_bool:
                    return False

                prev[level] = new_left_val

                if e.left:
                    q.append((e.left, level + 1))
                if e.right:
                    q.append((e.right, level + 1))

            return True
            
        return bfs()