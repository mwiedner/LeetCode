class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 1
        total = 0
        while n >= total:
            total+=i
            i+=1

        return i-2