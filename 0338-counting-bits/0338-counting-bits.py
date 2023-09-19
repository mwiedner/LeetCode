def numOnes(inp):
    length = len(inp)
    sum = 0
    
    i = 0
    while i < length:
        if inp[i] == "1":
            sum += 1
        i+=1
        
    return sum
        

def fromBinary(inp):
    sturr = str(inp)
    length = len(sturr)
    result = 0

    i = 0
    while i < length:
        if sturr[i] == "1":
            result += 2**(length-i-1)
        i+=1
    return result

def toBinary(inp):
    if inp == 0:
        return "0"

    i = 0
    while inp >= 2**i:
        i+=1
        
    maxExp = i
    minExp = i-1

    result = ""

    i = 0
    while i < maxExp:
        if inp >= 2**(minExp-i):
            result = result + "1"
            inp = inp - 2**(minExp-i)
        else:
            result = result + "0"
        i+=1

    return result

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        answer = []

        i = 0
        while i <= n:
            answer.append(numOnes(toBinary(i)))
            i+=1
        return answer