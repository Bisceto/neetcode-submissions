class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Need a set to check for duplicates
        char_set = set()
        # Need left and right pointer to measure the contiguous
        left = 0
        right = 0
        res = 0
        while right < len(s):
            char = s[right]
            # New char found, add to the set
            if char not in char_set:
                char_set.add(char)
            # Duplicate char found, need to shift left until it matches duplicate char, then shift by 1.
            else:
                while s[left] != char:
                    char_set.remove(s[left])
                    left += 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
