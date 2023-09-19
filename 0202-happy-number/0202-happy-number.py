def splice(n):
        strN = str(n)
        lengthN = len(strN)
        print(n)

        if (n == 4 or n == 2 or n == 3 or n == 5 or n == 6 or n == 8 or n == 9):
            return False
        
        i = 0
        sum = 0
        while i < lengthN:
            print(sum)
            print(int(strN[i])**2)
            sum+=int(strN[i])**2
            i+=1
        if sum == 1:
            print("TRIGGER ME")
            return True
        else:
            return splice(sum)

class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = splice(n)

        print(str(result))
        return result