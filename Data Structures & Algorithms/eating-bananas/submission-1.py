class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h >= len(piles)
        # upper bound for k is max(piles) i.e. every hour eat 1 pile. this is the FASTEST rate
        # for a pile of x bananas, it will take ceil(x / k) to finish.
        # len(piles) * ceil(x / k) <= h
        # ceil(x / k) <= h / len(piles)
        # we want to minimise k. 
        l = 1
        r = max(piles)
        res = float('inf')
        while l <= r:
            time_taken = 0
            mid = (l + r) // 2
            for pile in piles:
                time_taken += math.ceil(pile / mid) 
            if time_taken <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
