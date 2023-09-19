class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)

        i = 0
        sNumber = ''

        while i < length:
            sNumber += str(digits[i])
            i+=1
        
        number = int(sNumber)
        number+=1
        sNumber = str(number)

        digitto = []

        i = 0
        while i < len(sNumber):
            digitto.append(0)
            i+=1

        i = 0
        while i < len(sNumber):
            digitto[i] = int(sNumber[i])
            i+=1
        return digitto