class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        lst = []

        def checkPalindrome(substring):
            start = 0
            end = len(substring) - 1
            while start <= end:
                if substring[start] == substring[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True


        def helper(start):
            if start >= len(s):
                res.append(lst[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                isPalindrome = checkPalindrome(substring)
                if isPalindrome:
                    lst.append(str(s[start:end]))
                    helper(end)
                    lst.pop()
        
        helper(0)
        return res