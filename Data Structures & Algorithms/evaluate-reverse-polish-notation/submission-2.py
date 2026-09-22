class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operations = ["+", "-", "*","/"]
        for char in tokens:
            if char not in operations:
                st.append(int(char))
            else:
                if char == "+":
                    val2 = st.pop()
                    val1 = st.pop()
                    st.append(val1 + val2)
                if char == "-":
                    val2 = st.pop()
                    val1 = st.pop()
                    st.append(val1 - val2)
                if char == "*":
                    val2 = st.pop()
                    val1 = st.pop()
                    st.append(val1 * val2)
                if char == "/":
                    val2 = st.pop()
                    val1 = st.pop()
                    st.append(int(val1 / val2))
        return st[-1]