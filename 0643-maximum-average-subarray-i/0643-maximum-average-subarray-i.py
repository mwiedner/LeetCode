def getSum(nums):
    sum = 0.0
    i = 0
    while i < len(nums):
        sum += nums[i]
        i+=1
    return sum

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        windowSum = sum(nums[:k]) + 0.0
        bigSum = windowSum
        
        i = 0
        while (len(nums) - i) > k:
            windowSum = windowSum - nums[i] + nums[k+i]
            if windowSum > bigSum:
                bigSum = windowSum
            i+=1
        
        return bigSum / k