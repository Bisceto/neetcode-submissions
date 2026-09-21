class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx, val in enumerate(nums):
            # Optimisation check: if val > 0, all other values are also positive, cannot get 0 
            if idx == len(nums) - 2 or val > 0:
                break

            # Duplicated third number, will return duplicate triplet
            if idx != 0 and val == nums[idx - 1]:
                continue
            left = idx + 1
            left_val = None
            right = len(nums) - 1
            right_val = None
            while left < right:
                if nums[left] == left_val and nums[right] == right_val:
                    left += 1
                    right -= 1
                    continue
                two_sum = nums[left] + nums[right]
                if 0 - val == two_sum:
                    res.append([val, nums[left], nums[right]])
                    left_val = nums[left]
                    right_val = nums[right]
                    left += 1
                    right -= 1
                # Tuple needs to be bigger
                elif 0 - val > two_sum:
                    left += 1
                else:
                    right -= 1
        return res



            