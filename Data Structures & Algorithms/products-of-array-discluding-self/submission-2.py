class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_left = [1] * len(nums)
        for i in range(len(prefix_left)):
            if i == 0:
                continue
            else: 
                prefix_left[i] = prefix_left[i - 1] * nums[i - 1]
        prefix_right = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) -1:
                continue
            else:
                prefix_right[i] = prefix_right[i + 1] * nums[i+1]
        res = [0] * len(nums)
        for i in range(len(res)):
            res[i] = prefix_left[i] * prefix_right[i]
        return res