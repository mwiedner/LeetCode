class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        root = 0

        while x >= root:
            i+=1

            root = i * i

        return i-1