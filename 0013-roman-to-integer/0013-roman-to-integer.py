class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        chars = 0
        z = s + "0"
        while chars < len(z) - 1:
            
            reggie = 0

            if z[chars] == 'I':
                reggie = 1
            elif s[chars] == 'V':
                reggie = 5
            elif z[chars] == 'X':
                reggie = 10
            elif z[chars] == 'L':
                reggie = 50
            elif z[chars] == 'C':
                reggie = 100
            elif z[chars] == 'D':
                reggie = 500
            elif z[chars] == 'M':
                reggie = 1000

            reggie2 = 0
            
            if z[chars + 1] == 'I':
                reggie2 = 1
            elif z[chars + 1] == 'V':
                reggie2 = 5
            elif z[chars + 1] == 'X':
                reggie2 = 10
            elif z[chars + 1] == 'L':
                reggie2 = 50
            elif z[chars + 1] == 'C':
                reggie2 = 100
            elif z[chars + 1] == 'D':
                reggie2 = 500
            elif z[chars + 1] == 'M':
                reggie2 = 1000

            if reggie < reggie2:
                sum -= reggie
                print("Minus" + str(reggie))
            else: 
                sum += reggie
                print("Plus" + str(reggie))
            chars += 1
        return sum