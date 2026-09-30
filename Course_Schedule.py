# Time Complexity : O(V+E)
# Space Complexity : max(O(V+E))
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Using BFS. Initialize an indegree list and for each course as index increment the index by 1 in list
# Also maintain a HashMap for each vertices as key and values as the courses that are dependent on this key(that is course)
# Then iterate over the indegree list and check if the value of any course == 0, then append it to queue and increment count by 1
# Then iterate over the queue until it is empty and pop the vertices from the queue and check if that vertex exists in HashMap
# If it exists, get the values from the dict graph and decrement its value on that index in the indegree list by 1
# Again check if that indegree value == 0 then add it to the queue and increment the count by 1
# In the end check if count matches the num of courses if it doesnt return False else True


from collections import deque
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        count = 0
        graph = defaultdict(list) 
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            graph[prerequisites[i][1]].append(course)
            indegree[course] += 1
                
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            count += 1
            if node in graph:
                for value in graph[node]:
                    indegree[value] -= 1
                    if indegree[value] == 0:
                        queue.append(value)
        return count == numCourses

