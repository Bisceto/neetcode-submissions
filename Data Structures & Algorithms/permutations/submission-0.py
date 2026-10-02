class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pool = set(nums)
        lst = []
        def helper():
            if len(lst) == len(nums):
                res.append(lst[:])
                return
            # Cannot directly mutate the set while iterating over it. get a snapshot of it with list()
            for num in list(pool):
                lst.append(num)
                pool.remove(num)
                helper()
                lst.pop()
                pool.add(num)
        helper()
        return res