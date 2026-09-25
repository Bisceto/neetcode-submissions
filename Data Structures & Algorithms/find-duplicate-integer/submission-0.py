class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Key observation is that the number itself is within the range of len(nums). 
        # Meaning that the value can be an index. 
        # Treat the array as a linked list. use the val as an index to go to the next element

        slow = nums[0]
        fast = nums[0]

        while fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2= nums[slow2]

        return slow