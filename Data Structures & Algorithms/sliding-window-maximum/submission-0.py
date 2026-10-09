class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() #Queue of Indexes. This is a monotonic decreasing queue. bigger, older values are at the front
        for r in range(len(nums)):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            if q[0] <= r - k:
                q.popleft()
            if r >= k - 1:
                res.append(nums[q[0]])
        return res