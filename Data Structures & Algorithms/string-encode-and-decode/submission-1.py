class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s):
            delimiter_idx = s.find("#", idx)
            length = int(s[idx:delimiter_idx])
            print(length)
            res.append(s[delimiter_idx + 1 : delimiter_idx + 1 + length])
            idx = delimiter_idx + 1 + length
        return res

