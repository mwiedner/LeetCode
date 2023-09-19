class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        bigBoy = 0

        i = 0
        while i < len(candies):
            if candies[i] > bigBoy:
                bigBoy = candies[i]
            i+=1
        
        results = []

        i = 0
        while i < len(candies):
            if candies[i] + extraCandies >= bigBoy:
                results.append(True)
            else:
                results.append(False)
            i+=1
        return results