class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        strNum = str(num)
        length = len(strNum)

        sum = 0

        while length > 1:
            i = 0
            sum = 0
            while i < length:
                sum+= int(strNum[i])
                i+=1
            num = sum
            strNum = str(num)
            length = len(strNum)
        
        return num