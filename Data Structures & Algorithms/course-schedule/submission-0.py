class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)
        path = set()
        def dfs(course: int) -> bool:
            if course in path:
                return False

            if prereq[course] == []:
                return True
            path.add(course)

            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            
            path.remove(course)

            prereq[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True