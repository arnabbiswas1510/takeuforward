"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.
"""
from collections import deque
from typing import List


class SolutionBFS: #Same Kahn's Algorithm
    def canFinish(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        nodesVisited = 0 #You need this only for this problem since you are not doing Topo sort
        #Otherwise Kahn's doesnt need visited Nodes (DFS does)
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return nodesVisited == numCourses


class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #This solution uses the nodeid as implicit index for list of lists instead of using a map.
        # There is no extra benefit to this and I would have preferred to use a map
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        visit = [False] * numCourses
        def dfs(node, adj):
            # If the node is already in the stack, we have a cycle.
            if visit[node]:
                return False
            # Mark the current node as visited and part of current recursion stack.
            visit[node] = True
            for neighbor in adj[node]:
                if not self.dfs(neighbor):
                    return False #This is essential and you cant return True for if dfs() since you need to do below if True
            visit[node] = False
            adj[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True