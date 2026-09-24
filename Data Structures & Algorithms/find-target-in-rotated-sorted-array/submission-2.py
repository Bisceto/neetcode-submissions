class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # For every mid point, one part is sorted. one part is rotated
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r]:
                if target > nums[mid] and target <= nums[r]: #Must be in the right side
                    l = mid + 1
                else:
                    r = mid - 1
            else: #nums[mid] > nums[r]. # Left side is sorted
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
