class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        t0 = 0
        t1 = 1
        t2 = 1
        sum = 1

        i = 3
        while i <= n:
            sum = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = sum
            i+=1

        if n == 0:
            sum = 0
        return sum