def isContained(arra, inp):
        i = 0
        while i < len(arra):
            if inp == arra[i]:
                return True
            i+=1
        return False

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        tally = {}

        inputs = []

        i = 0
        while i < len(arr):
            if isContained(inputs, arr[i]):
                tally.update({arr[i]: tally.get(arr[i]) + 1})
            else:
                inputs.append(arr[i])
                tally.update({arr[i]: 1})
            i+=1
        
        length = len(tally)
        
        i = 0
        while i < length:
            j = 0 + i
            while j < length:
                if tally.get(inputs[j]) == tally.get(inputs[i]) and (i != j):
                    return False
                j+=1
            i+=1
        return True