from collections import deque

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        n = len(students)
        q = deque(students)

        res = n
        for sandwich in sandwiches:
            count = 0
            while count < n and q[0] != sandwich:
                curr = q.popleft()
                q.append(curr)
                count += 1
            if q[0] == sandwich:
                q.popleft()
                res -= 1
            else:
                break
        return res