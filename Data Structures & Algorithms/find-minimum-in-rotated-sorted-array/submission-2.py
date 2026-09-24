class Solution:
    def findMin(self, nums: List[int]) -> int:
        # how to determine the min? 
        # the index to the left is greater than it.
        # Idea is to find the "drop". 
        # n = len(nums)
        # l = 0
        # r = n - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     cur_val = nums[mid]
        #     # If the left num is greater, we found our min
        #     if nums[(mid + n - 1) % n] >= cur_val and cur_val <= nums[(mid + n + 1) % n]:
        #         return nums[mid]
        #     else:
        #         left_val = nums[l]
        #         right_val = nums[r]
        #         if cur_val < right_val:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        # return -1

        # Key observation: between every half, one half is the sorted part, the other part contains the rotation
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] >= nums[r]:
                l = mid + 1
        return nums[l]            


            