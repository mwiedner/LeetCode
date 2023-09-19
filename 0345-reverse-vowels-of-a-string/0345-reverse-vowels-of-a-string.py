def vowelTest(c):
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
        return True
    return False

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []

        listedString = list(s)

        i = 0
        while i < len(listedString):
            if vowelTest(listedString[i]):
                vowels.append(listedString[i])
                listedString[i] = "\U0001f913"
            i+=1
        
        vowels = vowels[::-1]

        i = 0
        j = 0
        while i < len(listedString):
            if listedString[i] == "\U0001f913":
                listedString[i] = vowels[j]
                j +=1
            i+=1
        
        result = ""
        i = 0
        while i < len(listedString):
            result += listedString[i]
            i+=1
        return result