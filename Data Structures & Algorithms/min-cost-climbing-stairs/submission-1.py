class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] is the min cost of climbing to the ith step
        n = len(cost)
        dp = [0] * (n + 1)
        # to climb to the 0 or 1 step is free.
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], #Take 1 step 
                        dp[i - 2] + cost[i - 2]) # Take 2 steps
        
        return dp[n]