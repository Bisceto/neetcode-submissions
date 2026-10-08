class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        hm_t = Counter(t)
        hm_s = defaultdict(int)
        have = 0 #Num of chars that match t
        required = len(hm_t.keys())
        l = 0
        best_len = float('inf')
        best_start = l
        for r in range(len(s)):
            char = s[r]
            hm_s[char] += 1
            if hm_s[char] == hm_t[char]:
                have += 1
            # Here, we have a valid window from l to r that is a substring
            while have == required:
                start_char = s[l]
                if r - l + 1 < best_len:
                    best_len = min(best_len, r - l + 1)
                    best_start = l
                if hm_s[start_char] == hm_t[start_char]:
                    have -= 1
                hm_s[start_char] -= 1
                l += 1

        if best_len == float('inf'):
            return ""
        return s[best_start: best_start + best_len]
