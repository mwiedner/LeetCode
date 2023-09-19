class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i = 0
        while i < len(nums):
            j = 0
            while j < len(nums):
                if nums[i] + nums[j] == target and i!=j:
                    result = []
                    result.append(i)
                    result.append(j)
                    return result
                j+=1
            i+=1