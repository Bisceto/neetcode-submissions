class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char in ['(', '{', '[']:
                st.append(char)
            elif char == ')':
                if st and st[-1] == '(':
                    st.pop()
                else:
                    return False
            elif char == '}':
                if st and st[-1] == '{':
                    st.pop()
                else:
                    return False
            elif char == ']':
                if st and st[-1] == '[':
                    st.pop()
                else:
                    return False
        return True if not st else False