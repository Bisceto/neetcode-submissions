class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        res = 0
        max_freq = 0
        left = 0
        right = 0
        for right in range(len(s)):
            char = s[right]
            hm[char] += 1
            max_freq = max(max_freq, hm[char])
            while (right - left + 1) - max_freq > k:
                hm[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            # If window is not valid anymore, we have to shrink the window
        return res
