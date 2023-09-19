class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
         return False
        return math.log10(n)/math.log10(4) % 1 == 0