class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        # 2^n subsets. For each element, either you pick or dont pick
        def helper(idx, lst):
            if idx == n:
                res.append(lst)
                return 
            else:
                helper(idx + 1, lst)
                helper(idx + 1, lst + [nums[idx]])
        
        helper(0, [])

        return res

            