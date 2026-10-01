class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sort the candidates so we can skip if we experience a duplicate number
        # Key Intuition: If i skip a number, i make sure i dont see it ever again in the path
        candidates.sort()
        def helper(idx, val, lst):
            if val == target:
                res.append(lst[:])
                return
            if idx == len(candidates) or val > target:
                return

            # Case 1: We pick the val
            lst.append(candidates[idx])
            helper(idx + 1, val + candidates[idx], lst)
            # Pop it to backtrack
            lst.pop()
            # Case 2: we dont pick the val. we fast forward the index to the next unique element
            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx + 1]:
                idx += 1
            helper(idx + 1, val, lst)



        helper(0, 0, [])
        return res
