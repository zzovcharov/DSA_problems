class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []

        for ch in logs:
            if ch == "../":
                if stack:
                    stack.pop()
            elif ch == "./":
                continue
            else:
                stack.append(ch)

        return len(stack)