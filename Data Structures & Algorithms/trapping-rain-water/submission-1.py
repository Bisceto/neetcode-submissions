class Solution:
    def trap(self, height: List[int]) -> int:
        # Formula to calculate water at a given index:
        # min(max left height, max right height) - height[i]
        # if negative, set as 0 (no water stored) so max(0, val above)

        # How can i find the max height to the left and to the right easily at any index? prefix sum array? We can include the current height in the prefix arrays too.
        # I.e. left[i]: the maximum height to the left of index i, including height[i] itself.
        left = [0] * len(height)
        right = [0] * len(height)
        left[0] = height[0]
        for i in range(1, len(height)):
                left[i] = max(height[i], left[i - 1])

        right[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
                right[i] = max(height[i], right[i + 1])
        res = 0 

        for i in range(len(height)):
            res += max(0, min(right[i], left[i]) - height[i])
        return res