class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while st and st[-1][1] < temp:
                prev_idx, prev_temp = st.pop()
                res[prev_idx] = idx - prev_idx
            st.append((idx, temp))
        return res