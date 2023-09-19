class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 0
        a = 0
        b = 1
        tempB = 0
        while i < n-1:
            tempB = b
            b = a + b
            a = tempB
            i+=1

        if n == 0:
            return 0
        
        return b