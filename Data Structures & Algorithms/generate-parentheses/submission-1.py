class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # You either pick an opening or closing. Need some conditions to see if can pick opening or closing 
        res = []
        lst = []

        def helper(opening, closing):
            # Base case
            if opening + closing == 2 * n:
                res.append(''.join(lst))
                return
            # Have enough openings: must be closing already
            if opening == n:
                lst.append(')')
                helper(opening, closing + 1)
                lst.pop()
            # Must have an opening
            elif opening == closing:
                lst.append('(')
                helper(opening + 1, closing)
                lst.pop()
            else:
                # Can pick either. Scenario 1, put another opening
                lst.append('(')
                helper(opening + 1, closing)
                lst.pop()
                # Scenario 2, put a closing
                lst.append(')')
                helper(opening, closing + 1)
                lst.pop()


        helper(0, 0)
        return res
