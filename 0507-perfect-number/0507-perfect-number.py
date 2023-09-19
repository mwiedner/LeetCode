def getDivisors(inny):
    divisors = []
    
    i = 2
    while i < inny**0.5:
        if inny % i == 0:
            divisors.append(i)
            divisors.append(int(inny / i))
        i+=1
    return divisors

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num == 1:
            return False

        divs = getDivisors(num)
        sum = 1
        for numbers in divs:
            sum+=numbers
        print(divs)
        print(sum)
        if sum == num:
            return True
        return False