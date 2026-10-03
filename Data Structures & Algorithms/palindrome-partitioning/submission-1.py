class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        lst = []

        # Start-End Inclsuvie
        def checkPalindrome(start, end):
            while start <= end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True


        def helper(start):
            if start >= len(s):
                res.append(lst[:])
                return
            
            for end in range(start, len(s)):
                isPalindrome = checkPalindrome(start, end)
                if isPalindrome:
                    lst.append(str(s[start:end + 1]))
                    helper(end + 1)
                    lst.pop()
        
        helper(0)
        return res