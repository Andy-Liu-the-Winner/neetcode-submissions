class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = []
        counter = 0
        for start, end in intervals:
            if not stack:
                stack.append((start, end))
            s, e = stack.pop()
            if start >= e:
                stack.append((s, e))
                stack.append((start, end))
            else:
                stack.append((start, min(e, end)))
        return len(intervals) - len(stack)