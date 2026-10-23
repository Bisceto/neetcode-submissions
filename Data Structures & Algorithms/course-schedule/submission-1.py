class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Do i need to count the seen courses? no! because if there is a course w no neighbours, means no prereq.
        # Idea is just to count if there is any impossible cycle. 
        graph = defaultdict(list)
        # 0 = unexplored, 1 = CYCLE detected, 2 = explored and okay
        state = [0] * numCourses

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(cur):
            if state[cur] == 2:
                return True
            elif state[cur] == 1:
                return False
            state[cur] = 1
            for nei in graph[cur]:
                if not dfs(nei):
                    return False
            state[cur] = 2
            return True

        for key in list(graph.keys()):
            valid = dfs(key)
            if valid:
                graph[key].clear()
            else:
                return False
            

        return True

        

