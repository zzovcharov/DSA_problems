class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_stack = []
        t_stack = []

        for ch in s:
            if ch != '#':
                s_stack.append(ch)
            else:
                if s_stack:
                    s_stack.pop()

        for ch in t:
            if ch != '#':
                t_stack.append(ch)
            else:
                if t_stack:
                    t_stack.pop()

        return s_stack == t_stack