class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            x, y = point
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(pq, (dist, x, y))
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(pq)
            res.append((x, y))
        return res