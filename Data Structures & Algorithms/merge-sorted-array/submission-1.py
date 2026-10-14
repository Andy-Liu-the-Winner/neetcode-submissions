class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr, l, r = m + n - 1, m - 1, n - 1

        while ptr != -1:
            if l == -1:
                # all r
                nums1[ptr] = nums2[r]
                r -= 1
            elif r == -1:
                # all l
                nums1[ptr] = nums1[l]
                l -= 1
            elif nums1[l] > nums2[r]:
                nums1[ptr] = nums1[l]
                l -= 1
            else:
                nums1[ptr] =nums2[r]
                r -= 1
            ptr -=1 