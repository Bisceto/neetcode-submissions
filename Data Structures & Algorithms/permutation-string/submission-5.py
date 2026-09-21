class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Quick optimisation
        if len(s1) > len(s2):
            return False
            
        # # Can't parse using pointers, because of permutations
        # hm1 = Counter(s1)
        # idx = 0
        # while idx < len(s2):
        #     char = s2[idx]
        #     if char in hm1:
        #         substring = s2[idx : idx + len(s1)]
        #         if Counter(substring) == hm1:
        #             return True
        #     idx += 1
        # return False

        hm1 = Counter(s1)
        req_matches = len(hm1.keys())
        print(req_matches)
        matches = 0
        left = 0
        right = 0
        hm2 = defaultdict(int)
        while right < len(s2):
            # Shrink left pointer
            if right - left + 1 > len(s1):
                if s2[left] in s1:
                    # If left points were a match before
                    if hm2[s2[left]] == hm1[s2[left]]:
                        matches -= 1 
                    hm2[s2[left]] -= 1
                    if hm2[s2[left]] == hm1[s2[left]]:
                        matches += 1
                left += 1
            if s2[right] in s1:
                # Do logic for now valid right pointer
                right_match_before = hm2[s2[right]] == hm1[s2[right]]
                hm2[s2[right]] += 1
                if hm2[s2[right]] == hm1[s2[right]]:
                    matches += 1
                    if matches == req_matches:
                        return True
                elif right_match_before:
                    matches -= 1
            # Increment right by 1
            right += 1
        return False