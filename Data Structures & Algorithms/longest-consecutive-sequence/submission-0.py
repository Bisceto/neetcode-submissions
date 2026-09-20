class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for val in nums_set:
            # True beginning
            if val - 1 not in nums_set:
                cur_res = 1
                cur_val = val
                while cur_val + 1 in nums_set:
                    cur_res += 1
                    cur_val += 1

                res = max(res, cur_res)
        return res