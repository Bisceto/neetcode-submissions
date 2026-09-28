class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = Counter(tasks)
        pq = list(hm.values())
        heapq.heapify_max(pq)
        # (task, time it is avail)
        waiting = deque()
        time = 0
        while pq or waiting:
            if waiting and time == waiting[0][1]:
                remaining , _ = waiting.popleft()
                heapq.heappush_max(pq, remaining)
            # Cur is the num left for this task
            if pq: 
                cur = heapq.heappop_max(pq)
                if cur > 1:
                    waiting.append((cur - 1, time + n + 1))
            time += 1
        return time

        