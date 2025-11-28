class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        max_dur = releaseTimes[0]
        best_key = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            dur = releaseTimes[i] - releaseTimes[i - 1]
            if dur > max_dur:
                max_dur = dur
                best_key = keysPressed[i]
            elif dur == max_dur and keysPressed[i] > best_key:
                best_key = keysPressed[i]

        return best_key

