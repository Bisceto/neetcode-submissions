class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        arr = stones
        while len(arr) > 1:
            stone1 = heapq.heappop_max(arr)
            stone2 = heapq.heappop_max(arr)
            if stone1 == stone2:
                continue
            else:
                heapq.heappush_max(arr, abs(stone1 - stone2))
        return 0 if len(arr) == 0 else arr[0]

