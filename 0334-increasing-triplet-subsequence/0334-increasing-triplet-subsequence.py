class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        i = 0
        a = nums[i]
        b = None
        c = None
        while i < len(nums):
            if nums[i] != a and b == None:
                b = nums[i]
            if nums[i] != a and nums[i] != b:
                c = nums[i]
            i+=1
        if c == None:
            return False
            

        i = 0
        while i < len(nums) - 2:
            candidate = nums[i]
            #print("Candidate: " + str(candidate))
            j = i + 1
            while j < len(nums) - 1:
                #print("J: " + str(nums[j]))
                if candidate < nums[j]:
                    k = j + 1
                    while k < len(nums):
                        #print("K: " + str(nums[k]))
                        if k < len(nums):
                            if nums[j] < nums[k]:
                                return True
                        k+=1
                j+=1
            i+=1
        return False