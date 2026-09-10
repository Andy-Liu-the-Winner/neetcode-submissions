class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s: return s
        remove_set = set()
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                if not stack:
                    remove_set.add(i)
                else:
                    stack.pop()
        remove_set.update(stack)
        s = "".join([char for idx, char in enumerate(s) if idx not in remove_set])

        return s