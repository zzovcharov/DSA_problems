class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = s.count('1')
        print("Number of '1's in the string:", c)
        return c  # return as well so you can use it programmatically


if __name__ == "__main__":
    # Read input from the console
    s = input("Enter a binary string (only 0s and 1s): ").strip()

    sol = Solution()
    result = sol.maximumOddBinaryNumber(s)
    print("Function returned:", result)
