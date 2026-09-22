class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st:
            self.min_st.append(val)
        else:
            self.min_st.append(val) if val <= self.min_st[-1] else None

    def pop(self) -> None:
        # Handle behaviour where if we pop the min_val
        pop_val = self.st.pop()
        if pop_val == self.min_st[-1]:
            self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
