def gcf(a, b):
    i = 1

    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a

    while i < big:
        if small % i == 0 and big % i == 0:
            result = i
        i+=1
    return result

def doesDivide(str, div):
    trial = ''

    i = 1
    while i < 1001:
        trial = div * i
        if trial == str:
            return True
        elif len(trial) > len(str):
            return False
        i+=1
    return False


def toString(listy):
    result = ""

    i = 0
    while i < len(listy):
        result += listy[i]
        i+=1
    return result


def getPrefixes(input, other, max):
    print("Input: " + input)
    print("Max:" + str(max))
    prefix = [] # Store all valid prefixes for a given input

    letters = [] # Store the letters that make up the prefix

    i = 0
    while i < len(input): # Loop through every letter in input
        letters.append(input[i]) # Add a letter

        if doesDivide(input, toString(letters)) and doesDivide(other, toString(letters)): # If the letters divides the input, it is a valid prefix
            prefix.append(toString(letters))
        i+=1

        if len(letters) == len(other):
            print("Error 1")
            return prefix

        if len(letters) * 2 > len(input) and input * 2 > other:
            print("Error 2")
            return prefix
        
        if len(prefix) == max and max != 0:
            print("Error 3")
            return prefix

    return prefix


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 == str2:
            return str1

        if doesDivide(str1, str1[0]):
            print("fdsafdsaaaa")
            if doesDivide(str2, str1[0]):
                print("FGDSAGFDSAG")
                return str1[0] * gcf(len(str1), len(str2))

        if len(str1) < len(str2):
            smallerString = str1
            other = str2
        else:
            smallerString = str2
            other = str1
        
        prefixesSmaller = getPrefixes(smallerString, other, 0)

        maxSize = len(prefixesSmaller)

        prefixesBigger = getPrefixes(other, smallerString, maxSize)

        prefixes1 = prefixesSmaller
        prefixes2 = prefixesBigger

        biggy = ""
        
        i = 0
        while i < len(prefixes1):
            j = 0
            while j < len(prefixes2):
                if prefixes1[i] == prefixes2[j] and len(prefixes1[i]) > len(biggy):
                    biggy = prefixes1[i]
                j+=1
            i+=1
        print(prefixes1)
        print(prefixes2)
        
        return biggy

        # We need to fix the code so that it gets the biggest prefix, checks if it works, and if it does, then closes