class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = None, None
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        #Do binary search on A (the smaller array)
        l, r = 0, len(A) - 1
        while True:
            mid = (l + r) // 2
            j = half - mid - 2 # Index of end of parition of B. Subtract 2 to account for the 0-based indexing of both arrs
            Aleft = A[mid] if mid >= 0 else float('-inf')
            Aright = A[mid + 1] if mid + 1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')
            if Aleft <= Bright and Bleft <= Aright:# Means we found less parition
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid - 1
            elif Bleft > Aright:
                l = mid + 1


