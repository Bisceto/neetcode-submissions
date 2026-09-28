class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        arr = nums
        while len(arr) > k:
            heapq.heappop(arr)
        return arr[0]