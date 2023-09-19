class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        chop = ''

        len1 = len(word1)
        len2 = len(word2)

        lillen = 0
        if len1 <= len2:
            lillen = len1
            big = word2
        else:
            lillen = len2
            big = word1
        

        i = 0
        while i < lillen:
            result += word1[i]
            result += word2[i]
            i+=1
        
        i = 0
        while i < abs(len1 - len2):
            chop += big[i + lillen]
            i+=1
        
        return result + chop