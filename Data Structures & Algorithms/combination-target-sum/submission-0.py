class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(idx, cur_sum, lst):
            if idx < len(nums):
                if cur_sum == target:
                    res.append(lst)
                elif cur_sum > target:
                    return
                else:
                    helper(idx + 1, cur_sum, lst)
                    helper(idx, cur_sum + nums[idx], lst + [nums[idx]])
            
        helper(0, 0, [])
        return res