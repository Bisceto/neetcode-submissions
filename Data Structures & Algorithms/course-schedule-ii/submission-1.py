class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Intuition: Similar to course schedule 1, we need to detect a cycle. if a cycle is detected, return empty array. else we return a path
        # State: 0 = unexplored, 1 = currently checking the path, 2 = explored and okay
        res = []
        graph = defaultdict(list)
        state = [0] * numCourses
        for course, prereq in prerequisites:
            graph[course].append(prereq) # We create the adj list inversely so when we do dfs the list is in order

        def dfs(key):
            if state[key] == 2:
                return True
            elif state[key] == 1:
                return False    
            else: #Unexplored key
                state[key] = 1
                for nei in graph[key]:
                    valid = dfs(nei)
                    if not valid:
                        return False
                state[key] = 2
                res.append(key)
                return True
        for cur in range(numCourses):
            valid = dfs(cur)
            if not valid:
                return []
        return res
            
        