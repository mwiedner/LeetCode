def selfDivCheck(num):
    numList = list(str(num))
    print numList
    
    i = 0
    while i < len(numList):
        if numList[i] == "0":
            return False
        elif num % int(numList[i]) != 0:
            return False
        i += 1
    return True

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []

        i = 0
        while i <= (right - left):
            if selfDivCheck(left + i):
                result.append(left + i)
            i+=1

        return result