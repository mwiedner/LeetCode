class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        divvy = 0
        half = n / 2.0

        if n == 1:
            return True
        elif n == 0:
            return False

        while divvy == 0:
            print(half)
            print("Divvy " + str(divvy))
            if half == 1.0:
                break
            divvy = half % 2
            half = half / 2.0
            
        
        if half == 1.0:
            return True
        else:
            return False