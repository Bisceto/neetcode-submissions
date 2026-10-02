class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        lst = []
        nums.sort()
        def helper(idx):
            if idx >= len(nums):
                res.append(lst[:])
                return
            
            # Case 1: Pick the value
            lst.append(nums[idx])
            helper(idx + 1)
            lst.pop()

            # Case 2: Dont pick the value, find the next unique value
            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            helper(idx + 1)

        helper(0)

        return res