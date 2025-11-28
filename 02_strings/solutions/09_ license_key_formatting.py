class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        cleaned = s.replace("-", "").upper()
        n = len(cleaned)
        if n == 0:
            return ""

        first = n % k or k
        chunks = [cleaned[:first]]
        for i in range(first, n, k):
            chunks.append(cleaned[i:i+k])
        result = "-".join(chunks)

        return result
