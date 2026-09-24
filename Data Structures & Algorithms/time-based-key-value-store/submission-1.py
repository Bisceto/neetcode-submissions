class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ls = self.hm[key]
        l = 0
        r = len(ls) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            val, ts = ls[mid]
            if ts == timestamp:
                res = val
                break
            elif ts > timestamp:
                r = mid - 1
            else: 
                res = val
                l = mid + 1
        return res
