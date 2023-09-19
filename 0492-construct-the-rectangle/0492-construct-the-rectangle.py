def getFactors(num):
    list = []
    i = 1
    while i <= num:
        if num % i == 0:
            list.append(i)
        i+=1
    return list

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        result = [0, 0]

        if area**(0.5) % 1 == 0:
            result[0] = int(area**(0.5))
            result[1] = int(area**(0.5))
            return result

        factors = getFactors(area)

        indie = len(factors) / 2

        result[1] = factors[indie - 1]
        result[0] = factors[indie]

        return result




