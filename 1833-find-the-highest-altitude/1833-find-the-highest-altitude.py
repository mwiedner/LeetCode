class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        startingAltitude = 0
        currentAltitude = startingAltitude
        highestAltitude = startingAltitude

        i = 0
        while i < len(gain):
            currentAltitude = currentAltitude + gain[i]
            if currentAltitude > highestAltitude:
                highestAltitude = currentAltitude
            i+=1

        return highestAltitude