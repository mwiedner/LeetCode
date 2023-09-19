def getLength(n):
    i = 0
    ip = 1
    while ip <= n:
        i+=1
        ip = 2**i
    return i

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        lengthA = len(a)
        lengthB = len(b)

        i = 0
        j = 0
        sumA = 0
        sumB = 0

        while i < lengthA:
            if a[i] == '1':
                sumA+= 2**(lengthA-i)
            i+=1


        while j < lengthB:
            if b[j] == '1':
                sumB+= 2**(lengthB-j)
            j+=1

        sumA /= 2
        sumB /= 2

        print("A: " + str(sumA) + "     B: " + str(sumB))

        sumC = sumA + sumB

        gL = getLength(sumC)

        print("gL is " + str(gL))
        print("sumC is " + str(sumC))

        binary_string = ''
        n = sumC
        while n > 0:
            remainder = n % 2
            binary_string = str(remainder) + binary_string
            n //= 2
        return binary_string if binary_string else '0'


