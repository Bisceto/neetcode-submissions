class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)
        pq = []
        for num, freq in hm.items():
            heapq.heappush(pq, (freq, num))
            if len(pq) > k:
                heapq.heappop(pq)
        return [num for (freq, num) in pq]