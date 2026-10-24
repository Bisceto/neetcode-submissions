class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Area is length x width. 
        # length is min(all the rectangles covered)
        # width is r - l + 1
        # Keep a monotonic increasing stack. append if height is >= top of stack 
        # While a bar is lesser than the top, we pop the max height. but when we push the cur height back, we use the 
        # leftmost index (to show that the last element that was popped, it could've still been extended using the cur height)

        st = []
        res = 0
        for idx, h in enumerate(heights):
            left_idx = idx
            while st and h < st[-1][1]: # the tallest height in the stack
                # We calculate what the tallest rectangle could have been
                tallest_idx, tallest_h = st.pop()
                left_idx = tallest_idx
                width = idx - tallest_idx
                res = max(res, width * tallest_h)
            st.append((left_idx, h))

        # Need to compute remaining elements in the stack. these are the bars that could extend all the way to the end
        n = len(heights)
        while st:
            idx, h = st.pop()
            res = max(res, h * (n - idx))

        return res