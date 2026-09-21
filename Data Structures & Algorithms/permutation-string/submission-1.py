class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Can't parse using pointers, because of permutations
        hm1 = Counter(s1)
        idx = 0
        while idx < len(s2):
            char = s2[idx]
            if char in hm1:
                substring = s2[idx : idx + len(s1)]
                if Counter(substring) == hm1:
                    return True
            idx += 1
        return False