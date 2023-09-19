class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        listy = list(s)

        while listy[0] == " ":
            print("Poo")
            del listy[0]
        while listy[len(listy) - 1] == " ":
            print("Pee")
            del listy[len(listy) - 1]

        i = 1
        while i < len(listy):
            if listy[i] == " " and listy[i-1] == " ":
                del listy[i]
                i-=1
            i+=1
        
        i = 0
        s = ""
        while i < len(listy):
            s += listy[i]
            i+=1

        splitten = s.split(" ")
        splitten = splitten[::-1]

        result = ""

        i = 0
        while i < len(splitten):
            result+= splitten[i]
            if i < len(splitten) - 1:
                result+= " "
            i+=1
        return result